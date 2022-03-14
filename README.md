# Baekjoon Online Judge
---

## 개요
PS<sup>Problem Solving</sup>를 공부하기 위해 백준의 알고리즘 문제를 해결하고 풀이 코드를 정리 해놓은 저장소입니다. 최대한 다양한 언어를 사용해보자라는 목적을 가지고 정리를 시작하는 만큼 해결한 문제의 수준이나 풀이 코드에 대한 질이 높지 않을 수 있습니다.

기본적으로 해당 저장소는 별다른 풀이나 전체적인 프로젝트 파일을 제공하지 않으며 소스코드만 제공됩니다.

다음과 같은 언어를 사용할 예정이며 대부분의 언어는 현재 시점(2022년 3월)을 기준으로 BOJ에서 제공하는 표준과 버전과 유사하게 환경이 구성되었습니다.

* C (C11)
* C++ (C++17)
* C# (6.0.101)
* Go (1.17.8)
* Java (15)
* Javascript (Node.js 16.14.0)
* Kotlin (1.6.1)
* Python3 (3.9.10)
* PHP (8.1.1)
* Rust 2018 (1.57.0)
* Scala (0.0.9)
* Swift (5.5.2)

## 환경 구성 
로컬에서 빌드및 테스트를 하기 위해서 다음과 같이 환경을 구성하였습니다.

### 하드웨어 사양 및 운영체제
* CPU: 1vCPU
* RAM: 1024MB
* OS: Ubuntu 20.04 LTS

### C
* 컴파일: `clang Main.c -o Main -O2 -Wall -lm -static -std=c11`
* 실행: `./Main`
* 버전: `12.0.0-3ubuntu1~20.04.5`

### C++
* 컴파일: `clang++ Main.c -o Main -O2 -Wall -lm -static -std=c11`
* 실행: `./Main`
* 버전: `12.0.0-3ubuntu1~20.04.5`

### C#
* 컴파일: `dotnet new console --force -o Main && dotnet publish Main --configuration Release --self-contained true --runtime linux-x64`
* 실행: `./Main`
* 버전: `6.0.201`

### Go
* 컴파일: `go build Main.go`
* 실행: `./Main`
* 버전: `go1.17.8 linux/amd64`
  
### Java
* 컴파일: `javac -release 15 -J-Xms1024m -J-Xmx1920m -J-Xss512m -encoding UTF-8 Main.java`
* 실행: `java -Xms1024m -Xmx1920m -Xss512m -Dfile.encoding=UTF-8 -XX:+UseSerialGC -DONLINE_JUDGE=1 -DBOJ=1 Main`
* 버전: `openjdk 17.0.2 2022-01-18 LTS`

### Javascript
* 실행: `node --stack-size=65536 Main.js`
* 버전: `v16.14.0`

### Kotiln
* 컴파일: `kotlinc-jvm -J-Xms1024m -J-Xmx1920m -J-Xss512m -include-runtime -d Main.jar Main.kt`
* 실행: `java -Xms1024m -Xmx1920m -Xss512m -Dfile.encoding=UTF-8 -XX:+UseSerialGC -jar Main.jar`
* 버전: `kotlinc-jvm 1.6.10 (JRE 17.0.2+8-LTS)`

### Python 3
* 컴파일: `python3 -c "import py_compile; py_compile.compile(r'Main.py')"`
* 실행: `python3 Main.py`
* 버전: `Python 3.8.10`

### PHP
* 컴파일: `php -l Main.php`
* 실행: `php -d display_errors=stderr Main.php`
* 버전: `PHP 8.1.3`

### Rust 2018
* 컴파일: `rustc --edition 2018 -O -o Main Main.rs`
* 실행: `./Main`
* 버전: `rustc 1.59.0 (9d1b2106e 2022-02-23)`

### Scala
* 실행: `scala-cli run Main.scala`
* 버전: `Scala 3.1.1`

### Swift
* 컴파일: `swiftc -O -o Main Main.swift`
* 실행: `./Main`
* 버전: `Swift version 5.5.3 (swift-5.5.3-RELEASE)`

## 진행 사항
* 단계별로 풀어보기: [구글 스프레드 시트](bit.ly/3sHxxDH)