# Nim Game
## _Tower breaker, revisited HackerRank_

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/HackerRank_logo.png/768px-HackerRank_logo.png)](https://www.hackerrank.com/challenges/tower-breakers-revisited-1/problem)

## Combinational Unpartial game
Nim is a mathematical game of strategy in which two players take turns removing (or "nimming") objects from distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap or pile. Depending on the version being played, the goal of the game is either to avoid taking the last object or to take the last object.
- Nim is a special case of a poset game where the poset consists of disjoint chains (the heaps).
- Nim is typically played as a misère game, in which the player to take the last object loses.

## Mathematical solution
The soundness of the optimal strategy described above was demonstrated by C. Bouton.
Theorem. In a normal Nim game, the player making the first move has a winning strategy if and only if the nim-sum of the sizes of the heaps is not zero. Otherwise, the second player has a winning strategy.

**Proof: Notice that the nim-sum (⊕) obeys the usual associative and commutative laws of addition (+) and also satisfies an additional property, x ⊕ x = 0.**

*Let x1, ..., xn be the sizes of the heaps before a move, and y1, ..., yn the corresponding sizes after a move. Let s = x1 ⊕ ... ⊕ xn and t = y1 ⊕ ... ⊕ yn. If the move was in heap k, we have xi = yi for all i ≠ k, and xk > yk. By the properties of ⊕ mentioned above, we have*

    t = 0 ⊕ t
      = s ⊕ s ⊕ t
      = s ⊕ (x1 ⊕ ... ⊕ xn) ⊕ (y1 ⊕ ... ⊕ yn)
      = s ⊕ (x1 ⊕ y1) ⊕ ... ⊕ (xn ⊕ yn)
      = s ⊕ 0 ⊕ ... ⊕ 0 ⊕ (xk ⊕ yk) ⊕ 0 ⊕ ... ⊕ 0
      = s ⊕ xk ⊕ yk
 
(*) t = s ⊕ xk ⊕ yk.
The theorem follows by induction on the length of the game from these two lemmas.*
**Lemma 1. If s = 0, then t ≠ 0 no matter what move is made.**
Proof: If there is no possible move, then the lemma is vacuously true (and the first player loses the normal play game by definition). Otherwise, any move in heap k will produce t = xk ⊕ yk from (*). This number is nonzero, since xk ≠ yk.

**Lemma 2. If s ≠ 0, it is possible to make a move so that t = 0.**
Proof: Let d be the position of the leftmost (most significant) nonzero bit in the binary representation of s, and choose k such that the dth bit of xk is also nonzero. (Such a k must exist, since otherwise the dth bit of s would be 0.) Then letting yk = s ⊕ xk, we claim that yk < xk: all bits to the left of d are the same in xk and yk, bit d decreases from 1 to 0 (decreasing the value by 2d), and any change in the remaining bits will amount to at most 2d−1. The first player can thus make a move by taking xk − yk objects from heap k, then
```
t = s ⊕ xk ⊕ yk           (by (*))
  = s ⊕ xk ⊕ (s ⊕ xk)
  = 0.
  ```
The modification for misère play is demonstrated by noting that the modification first arises in a position that has only one heap of size 2 or more. Notice that in such a position s ≠ 0, and therefore this situation has to arise when it is the turn of the player following the winning strategy. The normal play strategy is for the player to reduce this to size 0 or 1, leaving an even number of heaps with size 1, and the misère strategy is to do the opposite. From that point on, all moves are forced.

## Solution approach for HackerRank version
### Convert number into blocks
### using  binary xor to know the winner
