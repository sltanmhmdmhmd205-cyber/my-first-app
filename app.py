import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="MedLink",
    page_icon="🦷",
    layout="centered"
)

# 2. دعم اللغات المختلفة (قاموس الترجمة)
translations = {
    "العربية": {
        "title": "منصة MedLink",
        "subtitle": "ربط طلاب طب الأسنان بالمرضى وتحت إشراف الجامعات",
        "role_select": "اختر نوع حسابك:",
        "roles": ["مريض (بحث عن علاج)", "طالب طب أسنان", "دكتور مشرف / جامعة"],
        "camera_text": "التقط صورة لحالة الأسنان:",
        "submit_btn": "إرسال للذكاء الاصطناعي",
        "ai_processing": "جاري تحليل البيانات بواسطة الذكاء الاصطناعي...",
        "patient_match": "تم تحليل الحالة: تم توجيهك إلى طالب سنة رابعة (تخصص حشو جذور) بناءً على تقييم النظام.",
        "student_match": "تم مطابقة ملفك: يوجد 3 مرضى بحاجة للعلاج المطابق لمتطلباتك التدريبية اليوم.",
        "doctor_match": "مرحباً يا دكتور: يمكنك متابعة تقارير الطلاب ونسب التزام المرضى من اللوحة الرئيسية."
    },
    "English": {
        "title": "MedLink Platform",
        "subtitle": "Connecting dental students with patients under university supervision",
        "role_select": "Select your role:",
        "roles": ["Patient (Seeking Treatment)", "Dental Student", "Supervisor / University"],
        "camera_text": "Take a photo of your dental condition:",
        "submit_btn": "Submit to AI",
        "ai_processing": "Processing data via AI...",
        "patient_match": "Case Analyzed: You have been assigned to a 4th-year student (Endodontics) based on system evaluation.",
        "student_match": "Profile Matched: 3 patients found matching your training requirements today.",
        "doctor_match": "Welcome Doctor: You can now track student reports and patient adherence rates."
    }
}

# 3. القائمة الجانبية الاختيار اللغة
language = st.sidebar.selectbox("Language / اللغة", ["العربية", "English"])
t = translations[language]

# 4. واجهة المستخدم
st.title(t["title"])
st.caption(t["subtitle"])
st.divider()

# اختيار نوع المستخدم
user_role = st.selectbox(t["role_select"], t["roles"])

# التقاط الصورة عبر الكاميرا (إذا كان المستخدم مريضاً)
picture = None
if user_role in [t["roles"][0]]:
    st.write(t["camera_text"])
    picture = st.camera_input("Camera")

# 5. خوارزمية الذكاء الاصطناعي والمطابقة (Python)
if st.button(t["submit_btn"]):
    st.info(t["ai_processing"])
    
    # محاكاة لعمل الذكاء الاصطناعي بحسب الدور والصورة
    if user_role == t["roles"][0]:
        if picture is not None:
            st.success(t["patient_match"])
        else:
            st.warning("يرجى التقاط صورة للحالة أولاً ليتمكن الذكاء الاصطناعي من توجيهك.")
            
    elif user_role == t["roles"][1]:
        st.success(t["student_match"])
        
    elif user_role == t["roles"][2]:
        st.success(t["doctor_match"])
