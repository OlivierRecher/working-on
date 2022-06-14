package main.eraser;

public class EraserUn {
	
	/**
	 * Méthode avec regex
	 * @param req
	 * @return
	 */
	public static String start(String req) {
		// remplace tous les espaces qui n'ont pas d'espace avant et après par du vide
		return req.replaceAll("(?<! ) (?! )", ""); 
	}
}
