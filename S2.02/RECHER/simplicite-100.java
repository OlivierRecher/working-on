package eraser;

public class Eraser {
    public static String erase(String str) {
        StringBuilder sb = new StringBuilder(str);

		int indice = 0;
		while (indice < sb.length()) { 
			if(Character.isWhitespace(sb.charAt(indice)) 
					&& ((indice != 0 && indice != sb.length()-1 && !Character.isWhitespace(sb.charAt(indice+1)) && !Character.isWhitespace(sb.charAt(indice-1)))
						||(indice == 0 && !Character.isWhitespace(sb.charAt(indice+1)))
					    	|| (indice == sb.length()-1 && !Character.isWhitespace(sb.charAt(indice-1))))
					)  {
				sb.deleteCharAt(indice);
			} else {
				indice ++;
			}
		}
		str = sb.toString();
		return str;
    }
}
