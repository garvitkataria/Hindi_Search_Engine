package com.anurag.lucene.file;

import java.io.IOException;

public class SearchText {
	public static void main(String args[]) throws IOException{
		LuceneReadIndexFromFile ob1 = new LuceneReadIndexFromFile();
//		System.out.println("Args = "+args[0]);
//		System.out.println("Args = "+args[1]);
		ob1.searchText("लत"); 
	}
}
