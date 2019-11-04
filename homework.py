spell='Ala ma kota, kot ma Ale'
spellend='Arek woli psy a najbardziej boksery'
set_spell=set(spell)
set_spellend=set(spellend)
print("wspolne litery")
print(set_spell.intersection(set_spellend))
print("brakujące litery")
print(set_spellend.difference(set_spell))
spell_A=spell[0]
spell_e=spell[-1]
spell_k=spell[7]
spell_o=spell[8]
spell_l=spell[1]
spell_a=spell[2]
spell_=spell[3]
spell_r=ord(spell_a)+(114-97)
spell_w=ord(spell_a)+(119-97)
spell_i=ord(spell_a)+(105-97)
spell_p=ord(spell_a)+(112-97)
spell_s=ord(spell_a)+(115-97)
spell_y=ord(spell_a)+(121-97)
spell_n=ord(spell_a)+(110-97)
spell_b=ord(spell_a)+1
spell_d=ord(spell_a)+3
spell_z=ord(spell_a)+(122-97)
spell_j=ord(spell_a)+(106-97)
spell_s=ord(spell_a)+(115-97)

print (spell_A+chr(spell_r)+spell_e+spell_k+spell_+chr(spell_w)+spell_o+spell_l+chr(spell_i)+spell_+chr(spell_p)+chr(spell_s)+chr(spell_y)+spell_+spell_a+spell_+chr(spell_n)+spell_a+chr(spell_j)+chr(spell_b)+spell_a+chr(spell_r)+chr(spell_d)+chr(spell_z)+chr(spell_i)+spell_e+chr(spell_j)+spell_+chr(spell_b)+spell_o+
spell_k+chr(spell_s)+spell_e+chr(spell_r)+chr(spell_y))