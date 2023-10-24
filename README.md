![Screenshot 2023-10-24 132702](https://github.com/varunteja-18/ENCRYPTED-DUAL-IMAGE-REVERSIBLE-DATA-HIDING-TO-SECURE-PATIENT-INFORMATION-IN-E-HEALTHCARE/assets/109790641/65d5392a-7444-464d-bc84-c25cb8e04050)# ENCRYPTED DUAL-IMAGE REVERSIBLE DATA HIDING TO SECURE PATIENT INFORMATION IN E-HEALTHCARE

This project symbolize the innovative integration of cybersecurity methodologies, combining both cryptographic techniques and steganographic approaches, to enhance the security of patient information in the digital healthcare domain.  

▪️ <b>GRAYSCALE IMAGE</b><br>
▪️ <b>DICOM IMAGE</b><br>
▪️ <b>PAILLIER CRYPTOSYSTEM</b><br>
▪️ <b>DATA EMBEDDING</b><br>
▪️ <b>DATA EXTRACTION AND IMAGE RECOVERY</b><br>
▪️ <b>WATERMARK AUTHENTICATION</b><br>
▪️ <b>STATISTICAL ANALYSIS</b><br>
▪️ <b>HISTOGRAM ANALYSIS</b><br>

   
<ins>GRAYSCALE IMAGE:</ins><br>
A grayscale image is a type of picture that displays in shades of gray, without colors. It's similar to black and white photos we often see. In these images, pixel brightness indicates the shade, ranging from black to white. Typically, they are represented using 8 bits per pixel, allowing for 256 different shades. Grayscale images are common in image processing due to their simplicity, reduced data load, and the absence of color information.

<ins>DICOM IMAGE:</ins><br>
A DICOM image, standing for Digital Imaging and Communications in Medicine, is a standard format used to store and transmit medical imaging data. It not only contains the image but also pertinent patient and procedural information. DICOM images can vary in their bits per pixel, often 12 or 16 bits, allowing for detailed grayscale representations. This format is widely adopted in healthcare because of its comprehensive approach, ensuring both the image and accompanying data are encapsulated in one file.

<ins>PAILLIER CRYPTOSYSTEM:</ins><br>
The Paillier cryptosystem is a public-key encryption method. It stands out for its homomorphic traits, letting us perform calculations on encrypted data without decrypting it first. This feature makes Paillier valuable for secure computations and ensuring data privacy in numerous cryptographic scenarios. Furthermore, its adaptability allows integration with various cryptographic applications, and its robustness offers an added layer of security, minimizing potential vulnerabilities.

<ins>DATA EMBEDDING:</ins><br>
Initially, a 512x512 8-bit grayscale or 16-bit DICOM image is considered as the cover image, which is then divided into two parts virtually as coverimage1 and coverimage2. Each coverimage is encrypted using the Paillier cryptosystem. The patient information is treated as a confidential message, and zone values are computed following a specific algorithm. Subsequently, reduced secret and zone values are derived to prevent image distortion from an excessively large secret message. Both reduced secret and zone values are then encrypted using the Paillier cryptosystem. These encrypted reduced values are embedded in encrypted coverimage1 and encrypted coverimage2 to create stegoimage1 and stegoimage2, respectively, thereby forming a stego image.

<ins>DATA EXTRACTION AND IMAGE RECOVERY PHASE:</ins><br>
In the data extraction and image recovery phase, stegoimage1 and stegoimage2 are decrypted using the Paillier cryptosystem to successfully recover the original cover image and the confidential secret image.

<ins>WATERMARK AUTHENTICATION:</ins><br>
To further guarantee data authenticity and integrity, an 8-bit grayscale watermark image of 256x256 pixels is incorporated into the data during the embedding process using the Alpha-Blending method. This watermark acts as a distinct identifier.During data extraction and the image recovery phase, a Watermark Detection process is used to retrieve the watermark from the stego image and compare it to a reference image. If the watermarks align with eachother, it verifies the data's authenticity and integrity. Otherwise, any dissimilarity resembles that unauthorized changes have occurred.

In this comprehensive approach, encrypted dual image reversible data hiding is employed using 512x512 grayscale or DICOM images, supplemented by watermark authentication. This integrated strategy not only enhances the security of patient information within the realm of e-healthcare but also ensures both confidentiality and data integrity, providing a robust and reliable solution.

<ins>STATISTICAL METRICS:</ins><br>
To perfectly evaluate the performance of the specified algorithm, a range of metrics is employed, including Peak Signal-to-Noise Ratio (PSNR), Mean Square Error (MSE), Structural Similarity Index Matrix (SSIM), Normalized Absolute Error (NAE), Normalized Cross-correlation (NCC), Embedding Rate (bpp) and BER (Bit Error Rate). These metrics collectively provide insights into the algorithm's efficiency in terms of image quality, data preservation, and capacity.

<ins>HISTOGRAM ANALYSIS:</ins><br>
Histogram analysis is a method that visually charts the distribution of pixel intensities within an image. By presenting how often each pixel intensity occurs, it provides insights into the image's overall characteristics. Attackers frequently utilize histogram analysis to detect hidden information by putting together the histograms of the original (cover) and altered (stego) images. The strength and stealth of a data-hiding technique are often measured by how similar these two histograms are. A closer resemblance between the histograms suggests the hidden data is more effectively concealed, making it more resistant to detection. This evaluation plays a pivotal role in ensuring both the security of embedded data and the preservation of the cover image's integrity.

# OVERVIEW
![overview](https://github.com/varunteja-18/ENCRYPTED-DUAL-IMAGE-REVERSIBLE-DATA-HIDING-TO-SECURE-PATIENT-INFORMATION-IN-E-HEALTHCARE/assets/109790641/eebf777c-5d91-4655-ad50-06a56c396196)

![test_images](https://github.com/varunteja-18/ENCRYPTED-DUAL-IMAGE-REVERSIBLE-DATA-HIDING-TO-SECURE-PATIENT-INFORMATION-IN-E-HEALTHCARE/assets/109790641/2171ccc8-3318-4f1e-933f-888094136780)

![performance_metrics](https://github.com/varunteja-18/ENCRYPTED-DUAL-IMAGE-REVERSIBLE-DATA-HIDING-TO-SECURE-PATIENT-INFORMATION-IN-E-HEALTHCARE/assets/109790641/ed5dc058-b72f-49a8-9b05-e412bd70a774)

![Software requirements](https://github.com/varunteja-18/ENCRYPTED-DUAL-IMAGE-REVERSIBLE-DATA-HIDING-TO-SECURE-PATIENT-INFORMATION-IN-E-HEALTHCARE/assets/109790641/56d33273-e779-4e5f-bb50-fb718aee61dd)


# PAILLIER CRYPTOSYSTEM ALGORITHM
![paillier1](https://github.com/varunteja-18/ENCRYPTED-DUAL-IMAGE-REVERSIBLE-DATA-HIDING-TO-SECURE-PATIENT-INFORMATION-IN-E-HEALTHCARE/assets/109790641/32dccd45-0f56-4b1f-8805-4099d4679c31)
![paillier2](https://github.com/varunteja-18/ENCRYPTED-DUAL-IMAGE-REVERSIBLE-DATA-HIDING-TO-SECURE-PATIENT-INFORMATION-IN-E-HEALTHCARE/assets/109790641/0b19eaec-8016-40a8-bdfb-35cd1303a4e2)


# DATA EMBEDDING ALGORITHM
![data_embedding1](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/6afb42f8-5e16-4c25-8e23-2f5c46ee5c4f)
![data_embedding2](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/6207c4f7-9280-4d5c-baf8-cc473c29362e)
![data_embedding3](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/59e5c76c-3770-4ec8-ab21-7fab2090aa90)
![data_embedding4](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/2ea11993-297d-4566-b825-68dd6946a8e4)
![data_embedding5](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/85c52106-fc32-4138-9f2d-116731ed854f)
![data_embedding6](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/9f422705-5326-49e5-bc88-5c7055b0e36c)

# DATA EXTRACTION AND IMAGE RECOVERY ALGORITHM
![data_extraction_image_recovery1](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/ba0a741a-6ebb-4f93-9766-71ebe9a83c15)
![data_extraction_image_recovery2](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/1a4b823c-a976-431e-b8f5-8e06c21ef9f9)

# OUTPUT

![paillier_op](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/c853acb5-0e94-4f8a-a2db-658d6ea24f9f)

![op1](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/91efd224-d3c5-4ee8-985c-325171b06975)
![op2](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/4b4e5995-3ca7-4880-9ab9-0291b2b9443f)
![op3](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/cea0bfba-7cc5-4b7c-b106-2804e5e7003f)
![op4](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/ffe631ac-a5a4-457c-91af-5993bc8d0be4)
![op5](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/c69af05c-d366-424f-8b8f-62972b39066a)
![op6](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/5301f3bf-4d1e-4185-bbb7-81353dd19675)
![op7](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/9282d297-5217-471d-b192-9ddada5a5264)
![op8](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/614ebb5a-f8eb-4ffa-9122-cbd315b27122)
![op9](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/96a223a7-c4c4-4008-bb2b-a85282832887)
![op10](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/830f4bf4-d478-432e-9de7-f001d50c426b)
![op11](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/83829f73-3939-4e35-b30d-1b1b871c30f4)
![op12](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/93c34d37-a09c-42f6-963f-c97f1fe388f2)
![op13](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/2a6db5b4-c0fc-45c0-85b3-95adf42002cc)
![op14](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/ffbdb42f-1216-46fe-a042-75de24399777)

![OP15](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/8967e550-a3f5-4d01-8500-d159b9f9357f)
![op16](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/0d621954-3b93-4962-9e0f-fbb654ed6a72)
![op17](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/06ae4e21-600e-44e1-bd26-cae0ea7c3dfe)
![op18](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/68f6f7c0-32ff-4f76-8a1d-7dc6e13341c3)
![op19](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/752c2c92-f7a6-42cb-890a-d1de9bba634f)
![op20](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/e7367f63-49eb-4833-8b1f-49411e11bb21)
![op21](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/1e9a1c84-06be-42ca-9dc0-06c3ab101f9c)
![op22](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/94cb3ab4-bc85-4a00-9903-253e60cf3273)

![OP23](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/8706437c-e936-43a6-bbe4-7f20eec538ee)
![op24](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/027d1d24-a979-42ee-ba68-a2348d73e886)
![op25](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/c42cd156-43b5-44c5-9ffd-6bda8eccd70f)
![op26](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/8002cbfc-c7d1-4441-be98-a17a454bc590)
![op27](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/7b1abc8a-733e-442e-9325-f7ea75ee28b8)
![op28](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/ec6acdbf-c1e3-4f4b-b2b6-366a6692fc03)
![op29](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/86ff7ce0-a34f-481b-81e3-ab066e10ede0)
![op30](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/9392f8d7-12ca-40f7-b7e4-06c6e9b415f7)
![op31](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/e07a569a-6b7c-4946-83ba-7a167658a06c)

![op32](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/e96463a0-7eaf-4dfa-9397-f701e6beac61)
![op33](https://github.com/Neeraja-Kallamadi/Information_Security_E-Health_Encrypted_Dual-Image_Reversible_Data_Hiding/assets/110168775/c99641af-8eb3-446e-afa1-d7a4c5f1ebf0)

