import numpy as np
import pandas as pd
import nltk
import glob
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words('english')) 
ps = PorterStemmer()

unique_term=set()
terms_in_books=[]
col_list=[]
def find_doc_dictionary(file_path):
	#files = glob.glob("/home/aki/boolean_ir/IR/*.txt")
	files = glob.glob(file_path)
	for bookname in files:
		col_list.append(os.path.basename(bookname))
		file_open=open(bookname)
		read_file=file_open.read()
		token_words=nltk.word_tokenize(read_file)
		for word in token_words:
			unique_term.add(word)
	term=set()
	for w in unique_term:
		if w not in stop_words:
			stem_word=ps.stem(w)
			term.add(stem_word)
	for u_word in term:
		terms_in_books.append(u_word)
	term_len=len(term)
	scol=len(col_list)
	a = np.random.randint(0,1,size=(term_len,scol))
	df = pd.DataFrame(a, columns=col_list,index=terms_in_books)
	return df
def boolean_model(book_name,words):
	list_term=[]
	return_value=0
	book_open=open(book_name)
	read_book=book_open.read()
	bool_token_ws=nltk.word_tokenize(read_book)
	for  tkn in bool_token_ws:
		if tkn not in stop_words:
			st_word=ps.stem(tkn)
			list_term.append(st_word)
	if words in list_term:
		return_value=1
	return return_value
    
def vector_space_model(book_name,words):
	w_count=0
	list_term=[]
	return_value=0
	book_open=open(book_name)
	read_book=book_open.read()
	bool_token_ws=nltk.word_tokenize(read_book)
	for  tkn in bool_token_ws:
		if tkn not in stop_words:
			st_word=ps.stem(tkn)
			list_term.append(st_word)
	return_value=list_term.count(words)
	return return_value
        
    
print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
print("HH   ADDIS ABABA UNIVERISTY        HH")
print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
doc_path=str(input("Enter document path:"))
matrix=find_doc_dictionary(doc_path)
dirc_path = glob.glob(doc_path)

while 1:
	print("===============MENU=========================")
	x=int(input("Enter 1 for Boolean Model 2 for vector space Model"))
	if x==1:
                for book in dirc_path:
                        b_name=os.path.basename(book)
                        for uword in terms_in_books:
                                matrix.at[uword,b_name]=boolean_model(book,uword)
                print("=====BOOLEAN MODEL====")
                print(matrix)
	elif x==2:
                for book in dirc_path:
                        b_name=os.path.basename(book)
                        for uword in terms_in_books:
                                matrix.at[uword,b_name]=vector_space_model(book,uword)
                print("=====VECTOR SPACE MODEL====")
                print(matrix)
	else:
                print("Please enter the approprate choice 1 for Boolean 2 for Vector space model")
