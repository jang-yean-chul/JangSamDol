##메모리 DB사용 방법.


sqlite : 별도의 db 서버가 필요없이 db파일 기초하여 데이터베이스 처리하는 엔진이다.

import sqlite3

conn = sqlite3.connect(":memory:")

#conn = sqlite3.connect("c:/python/insa.db") #위에꺼는 메모리영역 이거는 파일로 생성

c = conn.cursor()

"""
실제 데이터는 디스크에 저장하는데 읽을떄는 메모리로 올려서 한다.

DML작업은 : 파스 -> 바인딩 -> 익스큐트
업데이트가 익스큐트로 끝나서 조회가 안되어서 여기에 리터닝절을 합쳐서 내놓은게 해결책이다.
sql은 컴파일을 해야한다. sql명령어를 담아두고 있는 영역을 커서라고 하는데 이를 sql작업영역이라 한다.

관련있는 블락을 모아두는것을 익센트라고 한다.
익센트를 모아둔게 테이블
테이블을 모아둔게 테이블스페이스
테이블스페이스가 모여있는게 디비

mssql,mysql은 다르다
테이블 스페이스가 없다.

db는 만들었다고 가정했을때 다음 작업은 테이블을 만들어야 한다.*오라클만 테이블스페이스가 있다.
"""

c.execute("create table emp(id integer,name text, sal integer)") #테이블 생성 integer은 숫자 ,text는 문자

c.execute("insert into emp(id,name,sal) values(1,'홍길동',1000)") #내부외부 " 와 ' 로 구분짓기
c.execute("insert into emp(id,name,sal) values(2,'박찬호',2000)") #내부외부 " 와 ' 로 구분짓기

c.execute("select * from emp") #객체 정보만 나온다(커서(디스크)에서 찾아왔다고 생각하면된다.)

c.fetchone() #fetch단계를 수행
#내부에 데이터가 있으면 하나씩하나씩(한개의 row씩) 나온다.

c.fetchall() #전부 동시에 송출!

#rollback이나 commit의 경우는 cursor가아니라 실제 메모리에 기반을둔 conn으로 작업을 해야한다.
conn.rollback() #트랜젝션 종료, insert,select는 커서를 기반으로 작업해서 사라진다.
conn.commit() #작업 저장

c.execute("insert into emp(id,name,sal) values(?,?,?)",(3,'나얼',3000))

insert_sql = "insert into emp(id,name,sal) values(?,?,?)"
c.execute(insert_sql,(4,'윤건',5000))
c.execute("select * from emp")
c.fetchall()

conn.commit()
c.close() #끝! 다 날라간다!
conn.close() #끝! 다 날라간다!




import sqlite3

#conn = sqlite3.connect(":memory:")

conn = sqlite3.connect("c:/python/insa.db") #위에꺼는 메모리영역 이거는 파일로 생성

c = conn.cursor()

c.execute("create table emp1(id integer,name text, sal integer)") #테이블 생성 integer은 숫자 ,text는 문자

c.execute("insert into emp1(id,name,sal) values(1,'홍길동',1000)") #내부외부 " 와 ' 로 구분짓기
c.execute("insert into emp1(id,name,sal) values(2,'박찬호',2000)") #내부외부 " 와 ' 로 구분짓기
c.execute("insert into emp1(id,name,sal) values(3,'나얼',3000)") #내부외부 " 와 ' 로 구분짓기
c.execute("insert into emp1(id,name,sal) values(4,'윤건',5000)") #내부외부 " 와 ' 로 구분짓기

c.execute("select name from sqlite_master where type = 'table'")
c.fetchall()

c.execute("PRAGMA table_info(emp1)")
c.fetchall()

c.execute("select * from emp1")
c.fetchall()

c.execute("select * from emp1")
c.fetchmany(2)

c.execute("create table dept1(deptid integer,name text, deptloc integer)") #테이블 생성 integer은 숫자 ,text는 문자

conn.commit()
c.close() #끝! 다 날라간다!
conn.close() #끝! 다 날라간다!




