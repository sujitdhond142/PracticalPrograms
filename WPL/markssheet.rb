puts "Enter your Name : "
name = gets.chomp
puts "Enter marks for subject 1"
sub1 = gets.to_i
puts "Enter marks for subject 2"
sub2 = gets.to_i
puts "Enter marks for subject 3"
sub3 = gets.to_i
total = sub1+sub2+sub3
average = total/3
puts "Name : #{name}"
puts "Total marks : #{total}"
puts "Average marks : #{average}"
if(average>=80)
	puts "Your Grade : A";
elsif(average >=60)
	puts "Your grade : B";
elsif(average>35)
	puts "Your Grade : c"
else
	puts "You failed"
end
