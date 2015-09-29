ROOT_DIR=.
COL=4 # 4 for estimated counts, 5 for transcripts per million
NUM_FILE=0

for f in $(find $ROOT_DIR -name "abundance.tsv" | sort);
do
  if [ $NUM_FILE = 0 ]; then
    HEADER=$(head -1 "$f" | cut -f$COL)
    IDS=$(cut -f1 "$f" | tail -n +2 | tr "\n" "\t")
    printf "$HEADER\t$IDS\n"
  fi
  SAMPLE_NAME=$(cut -d/ -f8 <<< "${f}")
  SAMPLE_DATA=$(cut -f$COL "$f" | tail -n +2 | tr "\n" "\t")
  printf "$SAMPLE_NAME\t$SAMPLE_DATA\n"
  NUM_FILE=$NUM_FILE+1
done;
