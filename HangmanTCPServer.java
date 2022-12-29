import java.io.DataOutputStream;
import java.io.File;
import java.io.IOException;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class HangmanTCPServer {

	public static void main(String[] args) throws Exception {
		System.out.println(InetAddress.getLocalHost());
		ServerSocket welcomeSocket = new ServerSocket(6789);
		while (true) {
			Socket connSocket = welcomeSocket.accept();
			Scanner inFromClient = new Scanner(connSocket.getInputStream());
			File file = new File("Word.txt");
			Scanner sc = new Scanner(file);
			Word word = new Word(sc);
			System.out.println(word.getWord());
			DataOutputStream outToClient = new DataOutputStream(connSocket.getOutputStream());
			outToClient.writeBytes(Integer.toString(word.getLength()) + '\n');
			String spots = "";
			Boolean miss = false;
			Boolean gameOver = false;
			while (true) {
				String guess1 = inFromClient.nextLine();
				if (guess1.equals("win")) {
					System.out.println("win");
					break;
				}
				if (guess1.equals("lose")) {
					System.out.println("lose");
					outToClient.writeBytes(word.getWord());
					connSocket.close();
					break;
				}
				System.out.println("Guessed character: " + String.valueOf(guess1));
				spots = word.getSpots(guess1.toCharArray()[0]);
				outToClient = new DataOutputStream(connSocket.getOutputStream());
				outToClient.writeBytes(spots + '\n');
			}
		}
	}
}