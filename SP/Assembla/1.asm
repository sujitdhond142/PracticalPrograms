PRGM	STRT	**	**
**	USNG	**	=15
**	LOAD	AX	=10
THRE	DCbb	3	**
FOUR	DCbb	4	**
**	LOAD	BX	FOUR
LOOP	ADDb	AX	BX
**	JNCb	LOOP	**
**	LOAD	CX	=9
LOOP	SUBb	CX	BX
**	JNZb	LOOP	**
**	MOVb	DX	=7
**	ADDb	BX	DX
**	ENDb	**	**