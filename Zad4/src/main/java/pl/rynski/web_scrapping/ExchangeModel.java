package pl.rynski.web_scrapping;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class ExchangeModel {
    private String code;
    private String rate;
    private String change;
    private String numberOfTransactions;
}
