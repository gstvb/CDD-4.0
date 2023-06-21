package fundamentos;

import java.util.Scanner;

public class exercicio07 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um numero:");
		double resp = entrada.nextDouble();
		
		if (resp > 0)
			System.out.println("Esse numero eh positivo.");
		else
			System.out.println("Esse numero eh negativo.");
	}

}
