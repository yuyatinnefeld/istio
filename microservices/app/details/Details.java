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

    static class MyHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            // Logging IP address of request to stdout
            System.out.println("Request received from: " + t.getRemoteAddress().toString());

            // Displaying json string
            String response = "{\"app\": \"details\", \"version\": \"1.0.0\", \"language\": \"java\"}";

            // Sending response
            t.sendResponseHeaders(200, response.length());
            OutputStream os = t.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}