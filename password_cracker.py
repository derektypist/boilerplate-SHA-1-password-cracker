import hashlib

# Set Up Dictionary
hash_dict = {}

def hash_10000_passwords(hash='',use_salts=False):
  # Apply File Handling
  with open('top-10000-passwords.txt') as f:
    for line in f.readlines():
      password = line.strip('\n ')
      if use_salts:
        with open('known-salts.txt') as f2:
          for salt in f2.readlines():
            salt = salt.strip('\n ')
            line1 = salt + password
            line1 = line1.encode('utf-8')
            h = hashlib.sha1(line1)

            line2 = password + salt
            line2 = line2.encode('utf-8')
            h2 = hashlib.sha1(line2)

            if (h.hexdigest() == hash or h2.hexdigest() == hash):
              return password
            
      else:
        line = line.strip('\n ').encode('utf-8')
        h = hashlib.sha1(line)
        hash_dict[password] = h.hexdigest()

  return hash_dict


def crack_sha1_hash(hash,use_salts=False):
    if (use_salts):
      return hash_10000_passwords(hash,use_salts)
    try:
      hash_dict = hash_10000_passwords(hash,use_salts)
      key_list = list(hash_dict.keys())
      val_list = list(hash_dict.values())
      hash_index = val_list.index(hash)
    except:
      return "PASSWORD NOT IN DATABASE"
    return key_list[hash_index]
    
