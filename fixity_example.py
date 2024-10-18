import hashlib
import os

def hash_file_in_chunks(file_path, hash_type="sha256", chunk_size=4096):
	if hash_type == "sha256":
		hash_func = hashlib.sha256()
	elif hash_type == "sha1":
		hash_func = hashlib.sha1()
	elif hash_type == "md5":
		hash_func = hashlib.md5()
	else:
		print (f"hash function {hash_type} not currently support - quitting.")
		quit()

	with open(file_path, 'rb') as f:
		while chunk := f.read(chunk_size):
			hash_func.update(chunk)    
	return hash_func.hexdigest()



my_file_a = r"C:\Users\User\Desktop\POWRR\OAIS.gif"
my_file_b = r"C:\Users\User\Desktop\POWRR\OAIS - Copy.gif"
my_file_c = r"C:\Users\User\Desktop\POWRR\OAIS_byte_changed.gif"
print (hash_file_in_chunks(my_file_a, hash_type="md5"), os.path.basename(my_file_a))
print (hash_file_in_chunks(my_file_b, hash_type="md5"), os.path.basename(my_file_b))
print (hash_file_in_chunks(my_file_c, hash_type="md5"), os.path.basename(my_file_c))

