
from mysql import connector
import datetime

class DB_Connect():
    def get_connected(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="321996",
                database="library_db",
            )
            return self.connection
        except Exception as e:
            print("Database connection error:", e)
            return None

class LibraryBookManager(DB_Connect):
    def get_object(self,id=None):
        try:
            self.connection =super().get_connected()

            if self.connection is None:
                return None

            self.cursor = self.connection.cursor()
            query = "select * from book where id =%s"
            values = (id,)

            self.cursor.execute(query, values)
            data = self.cursor.fetchone()

            self.cursor.close()
            self.connection.close()

            return data

        except Exception as e:
            print(e)
            return None

    def get(self):
        try:
            self.connection = super().get_connected()

            if self.connection is None:
                return

            self.cursor = self.connection.cursor()
            query = "select * from book"

            self.cursor.execute(query)
            data = self.cursor.fetchall()

            for i in data:
                print(i)

            self.cursor.close()
            self.connection.close()
            return data

        except Exception as e:
            print(e)

    def post(self,**kwargs):
        try:
            self.connection = super().get_connected()

            if self.connection is None:
                return

            self.cursor = self.connection.cursor()

            query = """insert into book(title,author,category,price,published_date) 
                       values(%s,%s,%s,%s,%s)"""
            values = [
                kwargs["title"],
                kwargs["author"],
                kwargs["category"],
                kwargs["price"],
                kwargs["published_date"]
            ]

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Book added Successfully.....!")

            self.cursor.close()
            self.connection.close()

        except Exception as e:
            print(e)
    def retrieve(self, id=None):
        try:
            data = self.get_object(id=id)

            if data is not None:
                print(data)
            else:
                print("Book doesn't exist..!")

        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            data = self.get_object(id=id)

            if data != None:

                self.connection = super().get_connected()

                if self.connection is None:
                    return

                self.cursor = self.connection.cursor()
                query = "delete from book where id=%s"
                values = (id,)

                self.cursor.execute(query, values)
                self.connection.commit()

                print("Deletion successfull..!")

                self.cursor.close()
                self.connection.close()
            else:
                print("Book doesn't exist..!")

        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            data = self.get_object(id=id)

            if data !=None:
                if not kwargs:
                    print("No data provided for update..!")
                    return

                allowed_fields = [
                    "title", "author", "category",
                    "price", "published_date"
                ]

                if not all(k in allowed_fields for k in kwargs):
                    print("Invalid column name..!")
                    return

                self.connection=super().get_connected()

                if self.connection is None:
                    return

                self.cursor=self.connection.cursor()
                placeholder =" "

                for k in kwargs.keys():
                    placeholder += k+"=%s, "
                placeholder = placeholder.rstrip(", ")

                query = f"update book set {placeholder} where id =%s"
                values = [v for v in kwargs.values()]
                values.append(id)

                self.cursor.execute(query,values)
                self.connection.commit()

                print("Updated successfully..!")

                self.cursor.close()
                self.connection.close()
            else:
                print("Book doesn't exist..!")

        except Exception as e:
            print(e)


library_instance = LibraryBookManager()

#library_instance.post(title="Python Basics",author="John Smith",category="Programming",price=450.00,published_date=datetime.date(2024, 1, 15))

#library_instance.post(
  #  title="Python Basics",
   # author="John Smith",
    #category="Programming",
    #price=450.00,
    #published_date=datetime.date(2024, 1, 15)
#)

#print(library_instance.get())
#library_instance.retrieve(id=2)
#library_instance.delete(id=1)
#library_instance.put(2,author="raghi")
#library_instance.put(2,title="Python Advanced",author="Ragendhu",price=850.00)
library_instance.put(2, category="Technology")
library_instance.get()