digit={
'1':'one','2':'two','3':'Three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten'

}

str1='123334645785658'

re=" ".join(digit[ch] for ch in str1 if ch.isdigit())

print(re)