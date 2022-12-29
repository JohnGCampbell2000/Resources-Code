import java.io.DataOutputStream;
import java.net.Socket;
import java.util.Arrays;
import java.util.Scanner;

public class HangmanTCPClient {

	public static void main(String[] args) throws Exception {
		Socket clientSocket = new Socket("localhost", 6789);
		Scanner inFromServer = new Scanner(clientSocket.getInputStream());
		String wordLength = inFromServer.nextLine();
		int wordsLength = Integer.parseInt(wordLength);
		GUI gui = new GUI(wordsLength);
		Scanner letters = new Scanner(System.in);
		Boolean miss = true;
		Boolean gameOver = false;
		String c = "";
		while (true) {
			if (!gameOver) {
				System.out.println("Guess by inputing a character: ");
				c = letters.nextLine();
			}
			DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
			outToServer.writeBytes(c + '\n');
			if (gameOver) {
				String word = inFromServer.nextLine();
				System.out.println(word);
				break;
			}

			String spots = inFromServer.nextLine();
			String[] spotsArray = spots.split(" ");
			if (spotsArray[0] != "") {
				for (String spot : spotsArray) {
					gui.addLetter(c.toCharArray()[0], Integer.parseInt(spot));
				}
			} else {
				miss = gui.addMiss(c);
			}
			if (!miss) {
				gameOver = true;
				c = "lose";
			} else if (!gui.isNotSolved()) {
				gameOver = true;
				c = "win";
			}
		}
	}
}
