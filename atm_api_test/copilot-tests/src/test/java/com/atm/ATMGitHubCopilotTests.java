package com.atm;

import io.restassured.http.ContentType;
import io.restassured.response.Response;

import static io.restassured.RestAssured.baseURI;
import static io.restassured.RestAssured.given;
import static org.junit.Assert.*;
// Had to ask GitHub Copilot to generate the following imports
import static org.hamcrest.Matchers.equalTo;

import org.json.JSONObject;
import org.junit.*;

/**
 * This class contains test methods for testing the ATM functionality.
 */
public class ATMGitHubCopilotTests {

    /**
     * Add the base URI for the ATM API.
     * Github Copilot did not generate this method.
     */
    @BeforeClass
    public static void setUp() {
        baseURI = "http://127.0.0.1:5000";
    }

    /**
     * Need to add the logout call after each test.
     * Github Copilot did not generate this method.
     */
    @After
    public void afterTest() {
        given().contentType(ContentType.JSON)
        .when()
        .post("/logout");
    }

    @Test
    public void testUserAuthorizationFail() {
        Response response = given()
                .param("username", "validUser")
                .param("password", "securePassword")
                .when()
                .post("/authorize");

        response.then().statusCode(415);
    }

    @Test
    public void testUserAuthorizationGood() {
        JSONObject body = new JSONObject();
        body.put("account_id", "2859459814");
        body.put("pin", "7386");
        Response response = given().contentType(ContentType.JSON).body(body.toString())
                .when()
                .post("/authorize");
        response.then().statusCode(200);
        assertNotNull(response.body().asString());
    }

    @Test
    public void testUserLogoutNone() {
        Response response = given().contentType(ContentType.JSON)
                .header("Authorization", "Bearer validAccessToken")
                .when()
                .post("/logout");

        response.then().statusCode(401);
    }

    @Test
    public void testUserLogoutGood() {
        JSONObject body = new JSONObject();
        body.put("account_id", "2859459814");
        body.put("pin", "7386");
        Response response = given().contentType(ContentType.JSON).body(body.toString())
                .when()
                .post("/authorize");
        response.then().statusCode(200);
        response = given().contentType(ContentType.JSON)
                .when()
                .post("/logout");
        response.then().statusCode(200);
    }

    @Test
    public void testWithdrawalBad() {
        Response response = given().contentType(ContentType.JSON)
                .header("Authorization", "Bearer validAccessToken")
                .param("amount", 100) // Withdrawal amount
                .when()
                .post("/withdraw");

        response.then().statusCode(400);
        // Validate updated account balance
    }

    @Test
    public void testWithdrawalGood() {
        JSONObject body = new JSONObject();
        body.put("account_id", "2859459814");
        body.put("pin", "7386");
        Response response = given().contentType(ContentType.JSON).body(body.toString())
                .when()
                .post("/authorize");
        body = new JSONObject();
        body.put("value", 100);
        response = given().contentType(ContentType.JSON).body(body.toString())
                .when()
                .post("/withdraw");

        response.then().statusCode(200);
        // Validate updated account balance
    }

    @Test
    public void testDeposit() {
        JSONObject body = new JSONObject();
        body.put("account_id", "2859459814");
        body.put("pin", "7386");
        Response response = given().contentType(ContentType.JSON).body(body.toString())
                .when()
                .post("/authorize");
        body = new JSONObject();
        body.put("amount", 200);
        response = given().contentType(ContentType.JSON).body(body.toString())
                .when()
                .post("/deposit");

        response.then().statusCode(200);
        // Validate updated account balance
    }

    @Test
    public void testGetAccountBalance() {
        JSONObject body = new JSONObject();
        body.put("account_id", "2859459814");
        body.put("pin", "7386");
        Response response = given().contentType(ContentType.JSON).body(body.toString())
                .when()
                .post("/authorize");
        response = given().contentType(ContentType.JSON)
                .header("Authorization", "Bearer validAccessToken")
                .when()
                .get("/balance");

        response.then().statusCode(200);
        // Extract and validate account balance
    }

    /**
     * Github Copilot generated this method.
     * Needed to add the authorize call before the history call.
     */
    @Test
    public void testTransactionHistory() {
        JSONObject body = new JSONObject();
        body.put("account_id", "2859459814");
        body.put("pin","7386");
        Response response = given().contentType(ContentType.JSON).body(body.toString())
                .when()
                .post("/authorize");
        response = given()
                .contentType(ContentType.JSON)
                .when()
                .get("/history");

        response.then().statusCode(200);
        // Validate transaction history structure
    }

    @Test
    public void testGetBalance() {
        given().param("accountNumber", "123456789")
                .when().get("/balance")
                .then().assertThat().statusCode(200)
                .body("balance", equalTo(1000));
    }

    @Test
    public void testWithdraw() {
        given().param("accountNumber", "123456789").param("amount", 200)
                .when().post("/withdraw")
                .then().assertThat().statusCode(200)
                .body("balance", equalTo(800));
    }
}