import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.IOException;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.List;

public class StockDataParser {

    public static List<StockRecord> parseCSV(String csvData) throws IOException {
        List<StockRecord> records = new ArrayList<>();
        try (StringReader reader = new StringReader(csvData);
             CSVParser csvParser = new CSVParser(reader, CSVFormat.DEFAULT.withFirstRecordAsHeader())) {

            for (CSVRecord csvRecord : csvParser) {
                StockRecord record = new StockRecord(
                        csvRecord.get("Date"),
                        Double.parseDouble(csvRecord.get("Open")),
                        Double.parseDouble(csvRecord.get("High")),
                        Double.parseDouble(csvRecord.get("Low")),
                        Double.parseDouble(csvRecord.get("Close")),
                        Double.parseDouble(csvRecord.get("Adj Close")),
                        Long.parseLong(csvRecord.get("Volume"))
                );
                records.add(record);
            }
        }
        return records;
    }
}

class StockRecord {
    private String date;
    private double open;
    private double high;
    private double low;
    private double close;
    private double adjClose;
    private long volume;

    public StockRecord(String date, double open, double high, double low, double close, double adjClose, long volume) {
        this.date = date;
        this.open = open;
        this.high = high;
        this.low = low;
        this.close = close;
        this.adjClose = adjClose;
        this.volume = volume;
    }

    // Getters and setters...
}
