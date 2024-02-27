import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.junit.BeforeClass;
import org.junit.Test;

import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

public class AtmAPITest {

    @BeforeClass
    public static void setUp() {
        RestAssured.baseURI = "https://your-atm-api-url.com";
        // Set any other common configurations here
    }

    @Test
    public void testUserAuthorization() {
        Response response = given()
                .param("username", "validUser")
                .param("password", "securePassword")
                .when()
                .post("/authorize");

        response.then().statusCode(200);
        // Extract and validate access token
        String accessToken = response.jsonPath().getString("access_token");
        // Add more assertions as needed
    }

    @Test
    public void testUserLogout() {
        Response response = given()
                .header("Authorization", "Bearer validAccessToken")
                .when()
                .post("/logout");

        response.then().statusCode(200);
        // Verify that the token is invalidated
    }

    @Test
    public void testWithdrawal() {
        Response response = given()
                .header("Authorization", "Bearer validAccessToken")
                .param("amount", 100) // Withdrawal amount
                .when()
                .post("/withdraw");

        response.then().statusCode(200);
        // Validate updated account balance
    }

    @Test
    public void testDeposit() {
        Response response = given()
                .header("Authorization", "Bearer validAccessToken")
                .param("amount", 200) // Deposit amount
                .when()
                .post("/deposit");

        response.then().statusCode(200);
        // Validate updated account balance
    }

    @Test
    public void testGetAccountBalance() {
        Response response = given()
                .header("Authorization", "Bearer validAccessToken")
                .when()
                .get("/balance");

        response.then().statusCode(200);
        // Extract and validate account balance
    }

    @Test
    public void testTransactionHistory() {
        Response response = given()
                .header("Authorization", "Bearer validAccessToken")
                .when()
                .get("/history");

        response.then().statusCode(200);
        // Validate transaction history structure
    }
}
