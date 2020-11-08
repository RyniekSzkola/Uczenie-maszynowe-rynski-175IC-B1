package pl.rynski.web_scrapping;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MainApi {

    private ScrapingService scrapingService;

    @Autowired
    public MainApi(ScrapingService scrapingService) {
        this.scrapingService = scrapingService;
    }

    @PutMapping("/exchange")
    public ResponseEntity<?> scrapRandomExchange() {
        return ResponseEntity.ok(scrapingService.scrapExchangeDataFromRandomCode());
    }

    @PutMapping("/links")
    public ResponseEntity<?> scrapLinksFromSite(@RequestBody String url) {
        return ResponseEntity.ok(scrapingService.scrapLinksFromRandomSite(url));
    }

    @PutMapping("/filmweb")
    public ResponseEntity<?> scrapFilmweb(@RequestBody String url) {
        return ResponseEntity.ok(scrapingService.scrapFilmInfoAndSaveToFile(url));
    }
}
