

## 1. Dataset
- This repo uses VNTC Dataset with 10 Topics: https://github.com/duyvuleo/VNTC

## 2. Run
- Tạo folder dataset and features:
```
./mkdir.sh
```

- Tiền xử lý data
```
python preProcessData.py
```

- Training
```
python main.py -m <model name>
```

- Dự đoán với mô hình được đào tạo trước và một tệp văn bản
```
python predict.py -i <filename document> -m <model name>
```
