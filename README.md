

## 1. Dataset
- Đề tài này sử dụng Bộ dữ liệu VNTC với 10 chủ đề: https://github.com/duyvuleo/VNTC

## 2. Run
- Tạo folder dataset và features:
```
./mkdir.sh
```

- Tiền xử lý data
```
python preProcessData.py
```

- Training
```
python main.py -m svm
```

- Dự đoán với mô hình được đào tạo trước và một tệp văn bản
```
python predict.py -i <filename document> -m svm
```
