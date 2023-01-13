### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:  #== operator should be used instead
      return True
    else  #missing : after else
      return False
   

  dif highest_card(self, card1 card2): #dif should be def #there should be a , between card1 card2 but card1 does not exist in the first place.
  if card1.value > card2.value:
    return card #is meant to be card1
  else:
    return card2
  


def cards_total(self, cards):
  total # need to set total to 0 to start with
  for card in cards:
    total += card.value
    return "You have a total of" + total #indentation incorrect #cant combine string and int like this
  
```
