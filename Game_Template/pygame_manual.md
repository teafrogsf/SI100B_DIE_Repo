1. **pygame.display.flip()**

   - **作用**：更新整个显示表面到屏幕。
   - **参数**：无。
   - **示例**：`pygame.display.flip()`

2. **pygame.sprite.Sprite**

   - **作用**：可见游戏对象的基类。

   - **参数**：无（用于创建子类）。

   - **示例**：

     ```python
     class Player(pygame.sprite.Sprite):
         def __init__(self):
             super().__init__()
     ```

3. **pygame.image.load(filename)**

   - **作用**：从文件加载图像。
   - **参数**：`filename` - 图像文件的路径字符串。
   - **示例**：`image = pygame.image.load('player.png')`

4. **pygame.font.Font(filename, size)**

   - **作用**：从文件创建一个新的字体对象。
   - **参数**：`filename` - 字体文件的路径字符串；`size` - 字体大小的整数。
   - **示例**：`font = pygame.font.Font('arial.ttf', 36)`

5. **pygame.Surface((width, height))**

   - **作用**：创建一个新的表面对象。
   - **参数**：`(width, height)` - 指定表面尺寸的元组。
   - **示例**：`surface = pygame.Surface((100, 100))`

6. **pygame.init()**

   - **作用**：初始化所有导入的 Pygame 模块。
   - **参数**：无。
   - **示例**：`pygame.init()`

7. **pygame.display.set_mode((width, height))**

   - **作用**：初始化用于显示的窗口或屏幕。
   - **参数**：`(width, height)` - 指定窗口尺寸的元组。
   - **示例**：`screen = pygame.display.set_mode((800, 600))`

8. **pygame.display.set_caption(title)**

   - **作用**：设置当前窗口标题。
   - **参数**：`title` - 窗口标题的字符串。
   - **示例**：`pygame.display.set_caption('游戏标题')`

9. **pygame.sprite.Group**

   - **作用**：用于存储和管理多个 Sprite 对象。
   - **参数**：无。
   - **示例**：`all_sprites = pygame.sprite.Group()`

10. **for event in pygame.event.get():**

    - **作用**：遍历事件队列。

    - **参数**：无。

    - **示例**：

      ```python
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
      ```

11. **pygame.transform.scale(surface, (width, height))**

    - **作用**：将表面缩放到新的分辨率。
    - **参数**：`surface` - 要缩放的表面；`(width, height)` - 新的尺寸。
    - **示例**：`scaled_surface = pygame.transform.scale(surface, (200, 200))`

12. **if keys[pygame.K_w] and self.rect.top > 0:**

    - **作用**：检查是否按下了 'W' 键并且矩形的顶部大于 0。
    - **参数**：`keys` - 按键状态数组；`self.rect.top` - 矩形的顶部位置。
    - **示例**：通常在游戏循环或更新方法中使用。

13. **pygame.time.Clock**

    - **作用**：创建一个用于跟踪时间的对象。
    - **参数**：无。
    - **示例**：`clock = pygame.time.Clock()`

14. **pygame.quit()**

    - **作用**：取消初始化所有 Pygame 模块。
    - **参数**：无。
    - **示例**：`pygame.quit()`

15. **keys = pygame.key.get_pressed()**

    - **作用**：获取所有键盘按钮的状态。
    - **参数**：无。
    - **示例**：`keys = pygame.key.get_pressed()`

16. **pygame.sprite.collide_rect(sprite1, sprite2)**

    - **作用**：根据它们的矩形检查两个精灵是否发生碰撞。
    - **参数**：`sprite1`, `sprite2` - 要检查碰撞的两个 Sprite 对象。
    - **示例**：`if pygame.sprite.collide_rect(player, enemy):`

17. **pygame.sprite.spritecollide(sprite, group, dokill)**

    - **作用**：检查一个精灵与组中的精灵是否发生碰撞。
    - **参数**：`sprite` - 要检查的 Sprite；`group` - 精灵组；`dokill` - 布尔值，如果为 True，则在发生碰撞时组中的精灵将被移除。
    - **示例**：`collided_sprites = pygame.sprite.spritecollide(player, enemies, False)`

18. **pygame.Color**
     - **作用**：表示颜色的对象，用于在Pygame中创建和管理颜色。

    - **参数**：可以接受多种输入，包括RGB元组、RGBA元组、颜色名称等。

    - **示例**：
    ```python
    import pygame
    red_color = pygame.Color(255, 0, 0)
    blue_color = pygame.Color('blue')
    green_color = pygame.Color(0, 255, 0, 128)
     ```

19. **pygame.cursors**
     - **作用**：提供了一组光标形状的常量，用于在Pygame中设置鼠标光标的形状。

    - **参数**：无（使用常量来指定不同的光标形状）。

    - **示例**：
    ```python
    import pygame
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
     ```


20. **pygame.draw**
     - **作用**：包含了用于绘制各种形状和图形的函数集合。

    - **参数**：具体参数根据不同的绘图函数而异，但通常包括表示表面、颜色、位置、大小等的参数。

    - **示例**：
    ```python
    import pygame
    display_surface = pygame.display.set_mode((800, 600))
    pygame.draw.rect(display_surface, (255, 0, 0), (50, 50, 100, 100))
    pygame.draw.circle(display_surface, (0, 0, 255), (200, 200), 50)
    pygame.draw.line(display_surface, (0, 255, 0), (300, 300), (400, 400), 5)
    pygame.display.flip()
     ```
21. **pygame.locals**
    - **作用**：包含了Pygame中用于处理事件和键盘鼠标输入的常量。
    - **参数**：该模块定义了各种事件类型、键盘键码以及鼠标按键等常量。
    - **示例**：
    ```python
    import pygame
    from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

    pygame.init()
    display_surface = pygame.display.set_mode((800, 600))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
    pygame.quit()
     ```

22. **pygame.Surface.copy**
    - **作用**：创建并返回一个表面的副本。
    - **参数**：无。
    - **示例**：
    ```python
    copied_surface = original_surface.copy()
     ```
    