;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Sun Jun 05 16:01:53 ICT 2022

.source test.java
.class public test
.super java/lang/Object

.field  caobahuy I

.method public <init>()V
.limit stack 1
.limit locals 1
.var 0 is this Ltest; from Label0 to Label1

Label0:
.line 7
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return

.end method

.method public static main([Ljava/lang/String;)V
.limit stack 2
.limit locals 1
.var 0 is arg0 [Ljava/lang/String; from Label0 to Label1

Label0:
.line 12
	getstatic java.lang.System.out Ljava/io/PrintStream;
	bipush 123
	invokevirtual java/io/PrintStream/println(I)V
Label1:
.line 13
	return

.end method
