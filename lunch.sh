
echo "Step 1: Preprocessing"
cat reviews_devset.json | python preprocess.py > processed_output.txt

echo "Step 2: Running Chi-Square MapReduce job"
python chi_square.py processed_output.txt > chi_output.txt

echo "Step 3: Running merging of top terms MapReduce job"
python combine_output.py chi_output.txt > merged.txt




echo "Job completed successfully"

