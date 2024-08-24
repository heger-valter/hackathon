import java.util.List;

public class SimpleMovingAveragePredictor {

    public static double calculateSMA(List<StockRecord> records, int period) {
        if (records.size() < period) {
            throw new IllegalArgumentException("Not enough data to calculate SMA");
        }

        double sum = 0;
        for (int i = 0; i < period; i++) {
            sum += records.get(i).getClose();
        }

        return sum / period;
    }

    public static void main(String[] args) throws IOException {
        String csvData = YahooFinanceAPI.fetchStockData("AAPL", "1609459200", "1672444800");
        List<StockRecord> records = StockDataParser.parseCSV(csvData);
        double sma = calculateSMA(records, 20);
        System.out.println("20-Day SMA: " + sma);
    }
}
