echo "Case 1 Test 1:"
cat case_1.txt | ./ch_h_v > test_outp.txt
diff test_outp.txt outp.txt

echo "Case 1 Test 2:"
cat case_1.txt | ./ch_h_v -v > test_outp.txt
diff test_outp.txt verbose_outp.txt

echo "Case 1 Test 3:"
./ch_h_v --filename=case_1.txt > test_outp.txt
diff test_outp.txt outp.txt

echo "Case 1 Test 4:"
./ch_h_v -v --filename=case_1.txt > test_outp.txt
diff test_outp.txt verbose_outp.txt

rm test_outp.txt