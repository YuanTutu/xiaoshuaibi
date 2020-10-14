# 获取到搜索按钮后点击
search_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/iq")))
search_btn.click()