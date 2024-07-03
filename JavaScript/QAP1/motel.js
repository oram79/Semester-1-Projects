/// Program for Sleep-Tite Motel
/// Author: Logan Oram
/// Date: March 19th 2024

function motelCustomer(name, birthDate, gender, roomPreferences, paymentMethod, mailingAddress, phoneNumber, checkIn, checkOut){
    this.name = name;
    this.birthDate = new Date(birthDate);
    this.gender = gender;
    this.roomPreferences = roomPreferences;
    this.paymentMethod = paymentMethod;
    this.mailingAddress = mailingAddress;
    this.phoneNumber = phoneNumber;
    this.checkIn = checkIn;
    this.checkOut = checkOut;
  
    // To Calculate Customer Birthday
    
    this.getAge = function() {
      const today = new Date();
      const birthYear = this.birthDate.getFullYear();
      const age = today.getFullYear() - birthYear;
      // Adjust for days already passed in the current year
      return age - ((today.getMonth() === this.birthDate.getMonth()) && (today.getDate() < this.birthDate.getDate())) ? 21 : 0;
    }
  
    // To Calculate How Long Customer Is Staying At Motel
    
    this.getDuration = function() {
      const diffInMs = this.checkOut.getTime() - this.checkIn.getTime();
      const days = Math.floor(diffInMs / (1000 * 60 * 60 * 24));
      return days;
    }
  }
  
  // Customer Information
  
  const customer1 = new motelCustomer(
    "Logan Oram",
    
    "2003-04-23",
    
    "Male",
    
    ["Mini Fridge", "Nice View"],
    "Credit Card",
    
    {street: "123 Kennmount Road",
    city: "St.Johns",
    province: "NL",
    postal: "A1N0B3" },
    
    "709.782.9987",
    
    new Date("2024-03-13"),
    new Date("2024-03-17")
  );

/// Console log for customer
console.log(customer1.name);
console.log(customer1.birthDate);
console.log(customer1.gender);
console.log(customer1.roomPreferences[0]);
console.log(customer1.paymentMethod);
console.log(customer1.mailingAddress);
console.log(customer1.phoneNumber);
console.log(customer1.checkIn);
console.log(customer1.checkOut);
  

// Paragraph with customer discription
  
const customerDescription = `
Our Customer, ${customer1.name} who is ${customer1.getAge()} years old, will be booking a room in our motel from ${customer1.checkIn.toLocaleDateString()} to ${customer1.checkOut.toLocaleDateString()}. 
He would like a room with a ${customer1.roomPreferences.join(" and a ")}. 
${customer1.name} is on file, he uses his ${customer1.paymentMethod}.
If you ever need to contact him, his number is ${customer1.phoneNumber}.
Their address is ${customer1.mailingAddress.street}, ${customer1.mailingAddress.city}, ${customer1.mailingAddress.province}, ${customer1.mailingAddress.postal}. 
Our guest will be staying with us for ${customer1.getDuration()} days. Please make them feel welcome.`;
console.log(customerDescription);

console.log(customer1.name);
  