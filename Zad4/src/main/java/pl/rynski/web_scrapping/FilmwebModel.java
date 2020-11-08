package pl.rynski.web_scrapping;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class FilmwebModel {
    private String url;
    private String director;
    private String premier;
    private String boxoffice;
    private String filmRating;
}
