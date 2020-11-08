package pl.rynski.web_scrapping;

import lombok.RequiredArgsConstructor;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFFont;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.annotation.Lazy;
import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Service;

import java.io.*;
import java.util.List;

@Service
public class ExcelService {
    private ScrapingService scrapingService;

    @Autowired
    public ExcelService(@Lazy ScrapingService scrapingService) {
        this.scrapingService = scrapingService;
    }

    @EventListener(ApplicationReadyEvent.class)
    public void createWorkbook() throws IOException {
        Workbook workbook = new XSSFWorkbook();

        CellStyle headerStyle = workbook.createCellStyle();
        headerStyle.setFillForegroundColor(IndexedColors.SKY_BLUE.getIndex());
        headerStyle.setFillPattern(FillPatternType.SOLID_FOREGROUND);

        XSSFFont font = ((XSSFWorkbook) workbook).createFont();
        font.setFontName("Arial");
        font.setFontHeightInPoints((short) 12);
        font.setBold(true);
        headerStyle.setFont(font);

        Sheet exchangeSheet = workbook.createSheet("Giełda");
        exchangeSheet.setColumnWidth(0, 5000);
        exchangeSheet.setColumnWidth(1, 5000);
        exchangeSheet.setColumnWidth(2, 5000);
        exchangeSheet.setColumnWidth(3, 5000);
        exchangeSheet.setColumnWidth(4, 5000);

        Row header = exchangeSheet.createRow(0);

        Cell headerCell = header.createCell(0);
        headerCell.setCellValue("Kod spółki");
        headerCell.setCellStyle(headerStyle);

        headerCell = header.createCell(1);
        headerCell.setCellValue("Cena");
        headerCell.setCellStyle(headerStyle);

        headerCell = header.createCell(2);
        headerCell.setCellValue("Kurs");
        headerCell.setCellStyle(headerStyle);

        headerCell = header.createCell(3);
        headerCell.setCellValue("Zmiana");
        headerCell.setCellStyle(headerStyle);

        headerCell = header.createCell(4);
        headerCell.setCellValue("Transakcje");
        headerCell.setCellStyle(headerStyle);

        CellStyle style = workbook.createCellStyle();
        style.setWrapText(true);

        Sheet linksSheet = workbook.createSheet("Linki");
        linksSheet.setColumnWidth(0, 5000);
        linksSheet.setColumnWidth(1, 5000);
        linksSheet.setColumnWidth(2, 5000);
        linksSheet.setColumnWidth(3, 5000);
        linksSheet.setColumnWidth(4, 5000);

        Row linksHeader = linksSheet.createRow(0);

        Cell linksHeaderCell = linksHeader.createCell(0);
        linksHeaderCell.setCellValue("Url");
        linksHeaderCell.setCellStyle(headerStyle);

        Sheet filmwebSheet = workbook.createSheet("Filmweb");
        filmwebSheet.setColumnWidth(0, 9000);
        filmwebSheet.setColumnWidth(1, 5000);
        filmwebSheet.setColumnWidth(2, 5000);
        filmwebSheet.setColumnWidth(3, 12000);
        filmwebSheet.setColumnWidth(4, 5000);

        Row filmwebHeader = filmwebSheet.createRow(0);

        Cell filmwebHeaderCell = filmwebHeader.createCell(0);
        filmwebHeaderCell.setCellValue("Url");
        filmwebHeaderCell.setCellStyle(headerStyle);

        filmwebHeaderCell = filmwebHeader.createCell(1);
        filmwebHeaderCell.setCellValue("Reżyser");
        filmwebHeaderCell.setCellStyle(headerStyle);

        filmwebHeaderCell = filmwebHeader.createCell(2);
        filmwebHeaderCell.setCellValue("Data premiery");
        filmwebHeaderCell.setCellStyle(headerStyle);

        filmwebHeaderCell = filmwebHeader.createCell(3);
        filmwebHeaderCell.setCellValue("Box office");
        filmwebHeaderCell.setCellStyle(headerStyle);

        filmwebHeaderCell = filmwebHeader.createCell(4);
        filmwebHeaderCell.setCellValue("Ocena filmu");
        filmwebHeaderCell.setCellStyle(headerStyle);

        File currDir = new File(".");
        String path = currDir.getAbsolutePath();
        String fileLocation = path.substring(0, path.length() - 1) + "rynski-175ic_b1.xlsx";
        FileOutputStream outputStream = new FileOutputStream(fileLocation);
        workbook.write(outputStream);
        workbook.close();

        scrapingService.scrapFilmInfoAndSaveToFile("https://www.filmweb.pl/film/Pearl+Harbor-2001-8586");
        scrapingService.scrapFilmInfoAndSaveToFile("https://www.filmweb.pl/film/Zielona+mila-1999-862");
        scrapingService.scrapFilmInfoAndSaveToFile("https://www.filmweb.pl/film/Droga-2009-419050");
    }

    public void appendFilmwebData(FilmwebModel filmwebModel) throws IOException {
        File file = new File("rynski-175ic_b1.xlsx");
        FileInputStream fip = new FileInputStream(file);
        Workbook workbook = WorkbookFactory.create(fip);
        Sheet sheet = workbook.getSheet("Filmweb");
        int rows = sheet.getPhysicalNumberOfRows();
        Row row = sheet.createRow(rows);
        Cell cell = row.createCell(0);
        cell.setCellValue(filmwebModel.getUrl());
        cell = row.createCell(1);
        cell.setCellValue(filmwebModel.getDirector());
        cell = row.createCell(2);
        cell.setCellValue(filmwebModel.getPremier());
        cell = row.createCell(3);
        cell.setCellValue(filmwebModel.getBoxoffice());
        cell = row.createCell(4);
        cell.setCellValue(filmwebModel.getFilmRating());

        try (FileOutputStream outputStream = new FileOutputStream("rynski-175ic_b1.xlsx")) {
            workbook.write(outputStream);
        }
        workbook.close();
    }

    public void appendLinksData(List<String> links) throws IOException {
        File file = new File("rynski-175ic_b1.xlsx");
        FileInputStream fip = new FileInputStream(file);
        Workbook workbook = WorkbookFactory.create(fip);
        Sheet sheet = workbook.getSheet("Linki");
        int rows = sheet.getPhysicalNumberOfRows();
        for (int i = 0; i < links.size(); i++) {
            Row row = sheet.createRow(rows + i);
            Cell cell = row.createCell(0);
            cell.setCellValue(links.get(i));
        }
        try (FileOutputStream outputStream = new FileOutputStream("rynski-175ic_b1.xlsx")) {
            workbook.write(outputStream);
        }
        workbook.close();
    }

    public void appendExchangeData(List<ExchangeModel> exchangeModels) throws IOException {
        File file = new File("rynski-175ic_b1.xlsx");
        FileInputStream fip = new FileInputStream(file);
        Workbook workbook = WorkbookFactory.create(fip);
        Sheet sheet = workbook.getSheet("Giełda");

        for (ExchangeModel exchangeModel : exchangeModels) {
            int rows = sheet.getPhysicalNumberOfRows();
            Row row = sheet.createRow(rows);
            Cell cell = row.createCell(0);
            cell.setCellValue(exchangeModel.getCode());
            cell = row.createCell(1);
            cell.setCellValue(exchangeModel.getRate());
            cell = row.createCell(2);
            cell.setCellValue(exchangeModel.getChange());
            cell = row.createCell(3);
            cell.setCellValue(exchangeModel.getNumberOfTransactions());
        }

        try (FileOutputStream outputStream = new FileOutputStream("rynski-175ic_b1.xlsx")) {
            workbook.write(outputStream);
        }
        workbook.close();
    }
}
