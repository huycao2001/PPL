.source D96Class.java
.class public D96Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_1
	istore_1
	iload_1
	iconst_2
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	getstatic java.lang.System.out Ljava/io/PrintStream;
	iconst_4
	invokevirtual java/io/PrintStream/print(I)V
	goto Label5
Label4:
	getstatic java.lang.System.out Ljava/io/PrintStream;
	iconst_3
	invokevirtual java/io/PrintStream/print(I)V
Label5:
Label1:
	return
.limit stack 5
.limit locals 2
.end method
