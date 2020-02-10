I wrote my program to run exactly as Brandt wants it to be run, so here's an example:

	>> python3 transposition-encr.py plain-text.txt keys.txt
	Encrypts the plain text file so that NO ONE can ever read it. Creates "plain-text.cipher".

	>> python3 asymmetrickey_encr.py public-key keys.txt
	Encrypts the keys file to be able to send to anyone. Creates "keys.cipher".

	>> python3 asymmetrickey_decr.py private-key keys.cipher
	This uses the private key to decrypt the encoded keys. Creates "keys.txt".

	>> python3 transposition-decr.py plain-text.cipher keys.txt
	Decrypts the encoded plain text file to be EXACTLY what it was when you started. Creates "plain-text.txt".

It takes files as arguments, which is easier than asking for them outright.

REQUIREMENTS:
"keys.txt" must be one line with two words separated by a single space. The two words must be greater than or equal to 10 characters long when duplicate characters are taken out.
"private-key" and "public-key" must be two integers on one line separated by a comma and a single space.
