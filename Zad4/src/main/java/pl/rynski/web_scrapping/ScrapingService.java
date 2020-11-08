package pl.rynski.web_scrapping;

import lombok.RequiredArgsConstructor;
import org.apache.commons.lang3.RandomStringUtils;
import org.apache.commons.validator.routines.UrlValidator;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class ScrapingService {

    private final ExcelService excelService;

    public FilmwebModel scrapFilmInfoAndSaveToFile(String url) {
        try {
            Document doc = Jsoup.connect(url).get();
            Element boxoffice = doc.getElementsByClass("boxoffice").first();
            Element director = doc.select("[itemprop=director]").first().select("[itemprop=name]").first();
            Element premier = doc.select(":containsOwn(premiera)").first().nextElementSibling().child(0).child(0);
            Element filmRating = doc.getElementsByClass("filmRating__rateValue").first();
            FilmwebModel filmwebModel = new FilmwebModel(url, director.text(), premier.text(), boxoffice.text() + " " + boxoffice.previousElementSibling().text() + " " + boxoffice.nextElementSibling().text(), filmRating.text());
            excelService.appendFilmwebData(filmwebModel);
            return filmwebModel;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public List<String> scrapLinksFromRandomSite(String url) {
        try {
            Document doc = Jsoup.connect(url).get();
            Elements links = doc.select("a[href]");
            List<String> result = new ArrayList<>();
            for (Element link : links) {
                String extractedLink = link.attr("href");
                if(UrlValidator.getInstance().isValid(extractedLink)) {
                    result.add(extractedLink);
                    if(result.size() >= 25) {
                        excelService.appendLinksData(result);
                        return result;
                    }
                }
            }
            excelService.appendLinksData(result);
            return result;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public List<ExchangeModel> scrapExchangeDataFromRandomCode() {
        try {
            List<ExchangeModel> result = new ArrayList<>();
            for (int i = 0; i < 5; i++) {
                String createdUrl;
                Document doc;
                ExchangeModel exchangeModel = new ExchangeModel();
                String randomCode = RandomStringUtils.randomAlphabetic(3).toLowerCase();
                createdUrl = "https://stooq.pl/q/?s=" + randomCode;
                doc = Jsoup.connect(createdUrl).followRedirects(true).get();
                if(!createdUrl.equals(doc.location())) {
                    Element redirectEl;
                    try {
                        redirectEl = doc.getElementById("f16").child(3).child(0).select("a[href]").first();
                        String newUrlPart = redirectEl.attr("href");
                        randomCode = newUrlPart.substring(5);
                        doc = Jsoup.connect("https://stooq.pl/" + newUrlPart).get();
                    } catch (NullPointerException e) {
                        System.out.println("EXCEPTION");
                        continue;
                    }
                }
                System.out.println(doc.location());
                System.out.println(randomCode);
                exchangeModel.setCode(randomCode);
                exchangeModel.setRate(doc.select("td:containsOwn(Kurs)").first().child(1).selectFirst("span").text());
                exchangeModel.setChange(doc.select("td:containsOwn(Zmiana)").first().child(1).child(0).select("span").get(1).text());
                exchangeModel.setNumberOfTransactions(doc.select("td:containsOwn(Transakcje)").first().selectFirst("span").text());
                result.add(exchangeModel);
            }
            excelService.appendExchangeData(result);
            return result;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
}
