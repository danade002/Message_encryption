#!/usr/bin/env python
# coding: utf-8

# In[4]:


def deencrypt(encrypted_message, key):
    alphabeth= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # key=3
    encrypted_message=encrypted_message.upper()
    original_message=''
    
    for encrypted_character in encrypted_message:
        new_deencrypted_character=''
        
        if encrypted_character in alphabeth:
            position=alphabeth.find(encrypted_character)-key
            if position<0:
                position=position+26
            new_deencrypted_character=new_dencrypted_character+alphabeth[position]
        else:
            new_deencrypted_character=encrypted_character
        original_message=original_message+ new_deencrypted_character
    # print(encrypted_message)
    return(original_message)
 
original_message=unencrypt(input('enter the encrypted character: '), 3)
print(original_message)


# In[ ]:





# In[ ]:




