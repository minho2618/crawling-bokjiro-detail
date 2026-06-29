import json

nb_path = 'crawling-bokjiro.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        src = "".join(cell['source'])
        
        # 1. 헬퍼 함수 셀 수정
        if 'def get_text_safe' in src and 'def click_safe' in src:
            new_src = """def get_text_safe(selector, by=By.CSS_SELECTOR):
    \"\"\"요소가 로드될 때까지 대기 후 텍스트를 반환합니다.\"\"\"
    try:
        element = wait.until(EC.presence_of_element_located((by, selector)))
        return element.text.strip()
    except Exception as e:
        return f"[Error] {e}"

def click_safe(selector, by=By.CSS_SELECTOR):
    \"\"\"요소가 클릭 가능해질 때까지 대기 후 JavaScript로 클릭합니다.\"\"\"
    try:
        element = wait.until(EC.element_to_be_clickable((by, selector)))
        # 화면에 안 보일 경우를 대비해 JS 클릭 사용
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2) # 클릭 후 렌더링 딜레이 반영
    except Exception as e:
        print(f"[Click Error] {e}")
"""
            cell['source'] = [line + '\n' for line in new_src.split('\n')[:-1]] + [new_src.split('\n')[-1]]
            
        # 2. 크롤링 본문 셀 수정
        if '# 1. 정책명' in src:
            new_src = """# 1. 정책명
policy_name = get_text_safe('#uuid-7o > div > div > div')
print("1. 정책명:", policy_name)

# 2. 정책설명
policy_desc = get_text_safe('#uuid-7r > div > div')
print("2. 정책설명:", policy_desc)

# 3. 담당부처
dept = get_text_safe('#uuid-7u > div > div')
print("3. 담당부처:", dept)

# 4. 기준연도
year = get_text_safe('#uuid-7x > div > div')
print("4. 기준연도:", year)

# 5. 문의처
contact = get_text_safe('#uuid-7z > div > div')
print("5. 문의처:", contact)

# 6. 지원주기
cycle = get_text_safe('#uuid-81 > div > div')
print("6. 지원주기:", cycle)

# 7. 제공유형
prov_type = get_text_safe('#uuid-83 > div > div')
print("7. 제공유형:", prov_type)

# 8. 지원대상
click_safe("//a[contains(text(), '지원대상')]", by=By.XPATH)
# 탭 클릭 후 나타나는 내용의 정확한 구조에 따라 아래 XPath를 조정할 수 있습니다.
target = get_text_safe("//a[contains(text(), '지원대상')]/ancestor::ul/following-sibling::div | //a[contains(text(), '지원대상')]/following::div[contains(@class, 'tab-content') or contains(@class, 'cont')][1]", by=By.XPATH)
print("\\n8. 지원대상:\\n", target)

# 9. 서비스 내용
click_safe("//a[contains(text(), '서비스 내용')]", by=By.XPATH)
service_content = get_text_safe("//a[contains(text(), '서비스 내용')]/ancestor::ul/following-sibling::div | //a[contains(text(), '서비스 내용')]/following::div[contains(@class, 'tab-content') or contains(@class, 'cont')][1]", by=By.XPATH)
print("\\n9. 서비스 내용:\\n", service_content)

# 10. 신청방법
click_safe("//a[contains(text(), '신청방법')]", by=By.XPATH)
apply_method = get_text_safe("//a[contains(text(), '신청방법')]/ancestor::ul/following-sibling::div | //a[contains(text(), '신청방법')]/following::div[contains(@class, 'tab-content') or contains(@class, 'cont')][1]", by=By.XPATH)
print("\\n10. 신청방법:\\n", apply_method)

# 11. 추가정보
click_safe("//a[contains(text(), '추가정보')]", by=By.XPATH)
additional_info = get_text_safe("//a[contains(text(), '추가정보')]/ancestor::ul/following-sibling::div | //a[contains(text(), '추가정보')]/following::div[contains(@class, 'tab-content') or contains(@class, 'cont')][1]", by=By.XPATH)
print("\\n11. 추가정보:\\n", additional_info)
"""
            cell['source'] = [line + '\n' for line in new_src.split('\n')[:-1]] + [new_src.split('\n')[-1]]

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)
