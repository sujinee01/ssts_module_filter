# 엑셀 파일 읽기
from google.colab import drive
import pandas as pd

# Google Drive 마운트
drive.mount('/content/drive')

# 파일 경로 지정
file_path = "/content/drive/My Drive/example.xlsx"  # Google Drive에 저장된 엑셀 파일 경로

# 엑셀 파일 읽기
data = pd.read_excel(file_path, engine='openpyxl')

# 열 이름 정리 (공백 제거)
data.columns = data.columns.str.strip()

# 데이터 확인
print("데이터 프레임의 첫 5개 행:")
print(data.head())
print("\n데이터 프레임의 열 이름:")
print(data.columns)

# 사용자 입력
filter_type = input("필터 유형을 선택하세요 (모듈 -> SSTS: 1, SSTS -> 모듈: 2): ")

# 결과 리스트 초기화
result = []

if filter_type == "1":
    # 모듈 -> SSTS
    selected_modules = input("모듈을 선택하세요 (예: A,B,C): ").split(',')
    
    for module in selected_modules:
        module = module.strip()  # 공백 제거
        if module in data.columns:
            # 해당 모듈과 관련된 SSTS 필터링
            module_ssts = data[data[module] == "x"]["module name"]
            for ssts in module_ssts:
                result.append({"SSTS": ssts, "Module": module})
        else:
            print(f"모듈 '{module}'은 데이터에 존재하지 않습니다.")

elif filter_type == "2":
    # SSTS -> 모듈
    selected_ssts = input("SSTS를 선택하세요 (예: 가,나,다): ").split(',')
    
    for ssts in selected_ssts:
        ssts = ssts.strip()  # 공백 제거
        if ssts in data["module name"].values:
            # 해당 SSTS와 관련된 모듈 필터링
            ssts_row = data[data["module name"] == ssts]
            for module in data.columns[2:]:  # 실제 모듈 열만 탐색
                if ssts_row[module].values[0] == "x":
                    result.append({"SSTS": ssts, "Module": module})
        else:
            print(f"SSTS '{ssts}'는 데이터에 존재하지 않습니다.")

else:
    print("잘못된 입력입니다. 프로그램을 종료합니다.")

# 결과를 데이터프레임으로 변환
result_df = pd.DataFrame(result).drop_duplicates()

# 결과 정렬 (SSTS와 Module을 기준으로 오름차순 정렬)
result_df = result_df.sort_values(by=["SSTS", "Module"]).reset_index(drop=True)

# 결과 출력
if not result_df.empty:
    print("\n필터링된 결과 (오름차순 정렬):")
    print(result_df)
else:
    print("선택한 조건과 관련된 결과가 없습니다.")
