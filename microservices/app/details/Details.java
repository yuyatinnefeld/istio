import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

public class Details {

    public static void main(String[] args) throws Exception {
        final int port = 7777;
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/", new MyHandler());
        server.setExecutor(null); // creates a default executor
        System.out.println("Serving on port 7777..\n");
        server.start();
    } 

    private static String setEnvOrDefault(String key, String defaultValue) {
        String value = System.getenv(key);
        return value != null ? value : defaultValue;
    }

    static class MyHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            // Logging IP address of request to stdout
            System.out.println("Request received from: " + t.getRemoteAddress().toString());

            // Reading environment variables with defaults
            String version = setEnvOrDefault("VERSION", "0.0.0");
            String message = setEnvOrDefault("MESSAGE", "MESSAGE_NOT_DEFINED");
            String env = setEnvOrDefault("ENV", "ENV_NOT_DEFINED");
            String podID = setEnvOrDefault("MY_POD_NAME", "PODID_NOT_DEFINED");

            // Creating json response
            String response = String.format(
                "{\"app\": \"details\", \"version\": \"%s\", \"message\": \"%s\", \"env\": \"%s\", \"podID\": \"%s\", \"language\": \"java\"}", 
                version, message, env, podID
            );

            // Sending response
            t.sendResponseHeaders(200, response.length());
            OutputStream os = t.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}
