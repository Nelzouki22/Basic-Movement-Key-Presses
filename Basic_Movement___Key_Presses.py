import pygame

# تهيئة مكتبة pygame
pygame.init()

# إعداد نافذة اللعبة بحجم 500x500 بيكسل
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("اللعبة الأولى")

# إعداد خصائص الشخصية (المستطيل)
x = 50       # الموقع الأفقي للشخصية
y = 50       # الموقع العمودي للشخصية
width = 40   # عرض الشخصية
height = 60  # طول الشخصية
vel = 5      # سرعة الحركة

# متغير للتحكم في استمرار اللعبة
run = True

# الحلقة الرئيسية للعبة
while run:
    # تأخير لتحديد سرعة اللعبة (100 ميللي ثانية بين كل إطار)
    pygame.time.delay(100)

    # معالجة الأحداث (مثل غلق النافذة)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # الحصول على حالة المفاتيح المضغوطة
    keys = pygame.key.get_pressed()

    # حركة الشخصية بناءً على المفاتيح المضغوطة
    if keys[pygame.K_LEFT]:
        x -= vel  # الحركة لليسار
    if keys[pygame.K_RIGHT]:
        x += vel  # الحركة لليمين
    if keys[pygame.K_UP]:
        y -= vel  # الحركة لأعلى
    if keys[pygame.K_DOWN]:
        y += vel  # الحركة لأسفل

    # تحديث الشاشة
    win.fill((0, 0, 0))  # ملء الشاشة باللون الأسود
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))  # رسم مستطيل أخضر يمثل الشخصية
    pygame.display.update()  # تحديث العرض

# إنهاء اللعبة وإغلاق نافذة pygame
pygame.quit()

