# AI Lab — Lab 5 Viva Cram Sheet (kal subah 10:45 wali lab se pehle)

## Numbers jo zubani yaad hone chahiye
- Dono trees ka **root value = 5** (Minimax aur Alpha-Beta, har order me — value kabhi nahi badalti)
- **Tree A** [3,5,2,9,0,7,0,0]: Minimax = 8 leaves, Alpha-Beta = **8 leaves** (yahan pruning **zero** — is order me faida nahi hua)
- **Tree B** [3,5,2,9,3,5,2,9]: Minimax = 8 leaves, Alpha-Beta = **6 leaves** (right MIN subtree ka doosra pair (2,9) skip ho gaya)
- **Sorted** [0,0,0,2,3,5,7,9]: Minimax = 8, Alpha-Beta = **6**

## 4 viva sawal (apne alfaz me)
1. **MAX MIN ke worst move ka assumption kyun rakhta hai?**
   Kyunki opponent bhi jeetna chahta hai. Us ke best reply ke against plan karna hi safe strategy hai — warna wo exploit kar lega.

2. **Alpha aur beta kya hain?**
   Alpha = MAX ko root se ab tak mila **sab se bara** score. Beta = MIN ko ab tak mila **sab se chhota** score. Ye wo window hai jisme result ab bhi badal sakta hai.

3. **Kya pruning se result badalta hai?**
   **Nahi.** Pruning sirf wo branches kaat ti hai jo root value par asar daal hi nahi sakti. Root value aur chosen move bilkul same rehte hain.

4. **Move ordering se pruning par farq kyun parta hai?**
   Achhi moves pehle aayein to alpha/beta jaldi tight ho jate hain, to baad wali branches alpha >= beta test par fail karke cut ho jati hain. Gandi ordering me bounds loose rehte hain — Tree A me is liye 8 ke 8 leaves evaluate hue.

## Ek line me edge case
Tree A me Alpha-Beta ne **8/8 leaves** evaluate kiye — matlab pruning guaranteed nahi hai. Worst case me Alpha-Beta = Minimax jitna kaam karta hai, zyada kabhi nahi.

## Trace ka flow (haath se batana ho to)
Leaves → depth-2 MAX (pair ka max) → depth-1 MIN (pair ka min) → root MAX (do values ka max). Tree B: leaves 3,5,2,9,3,5,2,9 → MAX level: 5,9,5,9 → MIN level: 5,5 → root: **5**.
