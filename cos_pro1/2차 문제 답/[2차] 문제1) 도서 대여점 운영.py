"""
< 문제 >
    [2차] 문제1) 도서 대여점 운영

< 문제 설명 >
    도서 대여점의 만화책과 소설책의 대여 요금이 다음과 같습니다.

    구분	    대여      요금	    추가 요금
    만화책	첫 2일    500원	    이후 1일당 200원씩 추가
    소설책	첫 3일    1000원	    이후 1일당 300원씩 추가

    만화책과 소설책의 대여 요금을 계산하기 위해 아래 그림과 같이 Book 인터페이스와 ComicBook, Novel 클래스를 작성했습니다.

    * Book :
      * Book은 책의 인터페이스입니다..
      * 책은 get_rental_price 함수를 구현해야 합니다.
      * get_rental_price 함수는 대여 기간을 매개변수로 받아 대여 요금을 계산합니다.
    * ComicBook :
      * ComicBook은 만화책을 나타내는 클래스이며, Book 인터페이스를 구현합니다.
      * get_rental_price 함수는 대여 기간을 매개변수로 받아 만화책의 대여 요금을 계산합니다.
    * Novel :
      * Novel은 소설책을 나타내는 클래스이며, Book 인터페이스를 구현합니다.
      * get_rental_price 함수는 대여 기간을 매개변수로 받아 소설책의 대여 요금을 계산합니다.

    대여를 원하는 책들의 종류가 들어있는 리스트 book_types와 대여 기간 day가 매개변수로 주어질 때,
    전체 대여 요금을 return 하도록 solution 함수를 작성하려고 합니다.
    위의 클래스 구조를 참고하여 주어진 코드의 빈칸을 적절히 채워 전체 코드를 완성해주세요.

< 매개변수 설명 >
    대여를 원하는 책들의 종류가 들어있는 리스트 book_types와 대여 기간 day가 solution 함수의 매개변수로 주어집니다.
    - book_types의 길이는 1 이상 50 이하입니다.
    - book_types에는 만화책을 뜻하는 문자열 "comic"과 소설책을 뜻하는 문자열 "novel"이 들어있습니다.
    - 예를 들어 ["comic", "comic", "novel"]이 매개변수로 주어진다면, 이는 만화책 두 권과 소설책 한 권을 나타냅니다.
    - day는 1 이상 100 이하의 자연수입니다.

< return 값 설명 >
    전체 대여 요금을 return 해주세요.
"""

from abc import *

class Book(metaclass=ABCMeta): # 추상 클래스 선언
	@abstractmethod # 추상 메서드 선언
	def get_rental_price(self, day):
		pass

class ComicBook(Book): # 추상 클래스를 불러와 구현
	def get_rental_price(self, day):
		cost = 500 # 비용
		day -= 2 # 대여일자(2일)
		if day > 0: # 대여일자 초과 시
			cost += day * 200 # 일당 200원 추가
		return cost

class Novel(Book): # ComicBook과 동일한 원리로 구현
	def get_rental_price(self, day):
		cost = 1000
		day -= 3
		if day > 0:
			cost += day * 300
		return cost

def solution(book_types, day):
	books = []
	for types in book_types: # 책의 종류를 순회
		if types == "comic": # 책의 종류가 comic일 경우
			books.append(ComicBook()) # comicBook 클래스를 이용하여 객체 생성
		elif types == "novel": # 책의 종류가 novel일 경우
			books.append(Novel()) # novel 클래스를 이용하여 객체 생성
	total_price = 0
	for book in books: # books의 요소들을 순회
		total_price += book.get_rental_price(day) # 대여비 계산 후 총합 누적
	return total_price
