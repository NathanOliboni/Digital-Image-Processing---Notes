# Digital-Image-Processing-Notes

## Color Spaces in Digital Image Processing

Color spaces (or color models) are mathematical models describing the way colors can be represented. They are essential in digital image processing for tasks like enhancement, segmentation, and conversion.

### 🌈 RGB (Red, Green, Blue)

- **Description**: The most common color space used in digital displays and cameras.
- **Components**: Red, Green, and Blue channels.
- **Usage**: Screen displays, image sensors, and digital cameras.
- **Model**: Additive — combining light to create colors.
- **Range**: Each channel typically ranges from 0 to 255 in 8-bit images.

> White = (255, 255, 255)  
> Black = (0, 0, 0)

---

### 🎥 YUV

- **Description**: Separates image luminance from chrominance.
- **Components**:
  - **Y**: Luminance (brightness)
  - **U** and **V**: Chrominance (color information)
- **Usage**: Video compression and broadcasting (e.g., PAL, NTSC).
- **Advantage**: Human vision is more sensitive to brightness than color, allowing compression of U and V.

---

### 🎨 CMY (Cyan, Magenta, Yellow)

- **Description**: Subtractive color model used in printing.
- **Relation to RGB**:
  - Cyan = 1 - Red
  - Magenta = 1 - Green
  - Yellow = 1 - Blue
- **Usage**: Basic model for printing and hardcopy devices.

---

### 🖨️ CMYK (Cyan, Magenta, Yellow, Key/Black)

- **Extension of CMY** with an additional **K (black)** component.
- **Why K?**: Combining CMY often does not produce a deep black; K helps improve contrast and save ink.
- **Usage**: Professional color printing.

---

### 🎛️ HSI (Hue, Saturation, Intensity)

- **Description**: Designed to align closely with human color perception.
- **Components**:
  - **Hue**: Type of color (angle on color wheel)
  - **Saturation**: Color purity
  - **Intensity**: Brightness level
- **Usage**: Image analysis and segmentation.

---

### 🎚️ HSL (Hue, Saturation, Lightness)

- **Similar to HSI**, but uses **Lightness** instead of Intensity.
- **Components**:
  - **Hue**: Color type
  - **Saturation**: Vividness of color
  - **Lightness**: Average of max and min RGB values
- **Usage**: Color manipulation in graphics software.

---

### 🧪 HSV (Hue, Saturation, Value)

- **Also known as HSB (Hue, Saturation, Brightness)**.
- **Components**:
  - **Hue**: Color angle (0–360°)
  - **Saturation**: From gray to full color
  - **Value**: Brightness from black to color
- **Usage**: Widely used in image editing and computer vision for intuitive color filtering.

---

### 📌 Summary Table

| Model | Type       | Components         | Common Use                   |
|-------|------------|--------------------|------------------------------|
| RGB   | Additive   | Red, Green, Blue   | Screens, cameras             |
| YUV   | Hybrid     | Luminance, Chroma  | Video compression            |
| CMY   | Subtractive| Cyan, Magenta, Yellow | Printing basics          |
| CMYK  | Subtractive| CMY + Black        | Professional printing        |
| HSI   | Perceptual | Hue, Saturation, Intensity | Image analysis     |
| HSL   | Perceptual | Hue, Saturation, Lightness | Graphic design     |
| HSV   | Perceptual | Hue, Saturation, Value | Computer vision       |
