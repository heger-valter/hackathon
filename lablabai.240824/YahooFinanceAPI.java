import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

import java.io.IOException;

public class YahooFinanceAPI {

    private static final String BASE_URL = "https://query1.finance.yahoo.com/v7/finance/download/";

    public static String fetchStockData(String ticker, String startDate, String endDate) throws IOException {
        OkHttpClient client = new OkHttpClient();

        String url = BASE_URL + ticker + "?period1=" + startDate + "&period2=" + endDate + "&interval=1d&events=history";

        Request request = new Request.Builder()
                .url(url)
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                throw new IOException("Unexpected code " + response);
            }

            return response.body().string();
        }
    }
}
