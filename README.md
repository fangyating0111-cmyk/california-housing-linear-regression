# 🏠 California Housing Price Prediction (Linear Regression)

## 📌 项目简介

本项目基于经典的 **California Housing 数据集**，构建了一个完整的数据分析与机器学习流程，最终使用**线性回归模型（Linear Regression）**对房价进行预测。

项目涵盖了从数据预处理、特征工程到模型训练与评估的完整 pipeline，适合作为机器学习入门实践项目或数据科学作品展示。

---

## 🎯 项目目标

* 理解机器学习项目的完整流程
* 掌握数据清洗与特征工程方法
* 使用线性回归进行建模与预测
* 学会用 GitHub 管理项目并进行版本控制

---

## 📊 数据集说明

* 数据来源：Scikit-learn 内置数据集
* 样本数量：20640 条
* 特征数量：8 个
* 目标变量：`MedHouseVal`（房价中位数）

### 主要特征：

| 特征名        | 含义     |
| ---------- | ------ |
| MedInc     | 收入中位数  |
| HouseAge   | 房龄     |
| AveRooms   | 平均房间数  |
| AveBedrms  | 平均卧室数  |
| Population | 人口     |
| AveOccup   | 平均居住人数 |
| Latitude   | 纬度     |
| Longitude  | 经度     |

---

## 🧱 项目结构

```
california-housing-linear-regression/
│
├── data/                # 数据存储
├── models/              # 保存训练好的模型
├── notebooks/           # Jupyter Notebook分析
├── reports/             # 输出报告
│
├── src/
│   ├── data_preprocessing.py   # 数据清洗
│   ├── feature_engineering.py  # 特征工程
│   ├── train.py                # 模型训练
│   └── evaluate.py             # 模型评估
│
├── requirements.txt
└── README.md
```

---

## ⚙️ 环境配置

### 1️⃣ 创建虚拟环境（推荐）

```bash
python -m venv venv
```

激活环境：

```bash
venv\Scripts\activate
```

---

### 2️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

---

## 🚀 运行项目

```bash
python src\train.py
```

---

## 🧠 模型方法

本项目使用：

* **线性回归（Linear Regression）**

模型公式：

[
y = wX + b
]

---

## 🧹 数据处理流程

1. 数据加载
2. 数据清洗（去异常值）
3. 特征选择
4. 数据划分（Train/Test）
5. 模型训练
6. 模型预测
7. 模型评估

---

## 📈 模型评估

使用指标：

* **MSE（均方误差）**
* **R²（决定系数）**

示例输出：

```
MSE: 0.52
R2: 0.61
```

---

## ✨ 项目亮点

* ✅ 完整机器学习流程（从数据到模型）
* ✅ 模块化代码结构（工程化设计）
* ✅ 使用标准评估指标
* ✅ 支持扩展（可加入更多模型）

---

## 🔧 可改进方向

* 使用更多模型（如 Ridge / Lasso / Random Forest）
* 加入特征标准化（StandardScaler）
* 使用交叉验证（Cross Validation）
* 模型持久化（保存与加载）
* 构建简单 API（如 Flask）

---

## 📦 模型保存（可选）

```python
import joblib
joblib.dump(model, 'models/model.pkl')
```

---

## 👨‍💻 作者

* Name: 枫叶糖
* GitHub: https://github.com/fangyating0111-cmyk

---

## ⭐ 如果这个项目对你有帮助

欢迎点一个 Star ⭐ 支持一下！

---
