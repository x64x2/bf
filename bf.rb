#  bf.rb
#  
#  Copyright 2025 x64x2 <x64x2@mango>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

### this module defines brainfuck interpreter
require "socket"			#load socket lib


include DstructBf			#inheriting Basic Datastructure for Bf

class Bf        #basic turing machine data structure
   ptr = []
   

   def init(bf);
     @bf, @machine, @ptr = [0]*30000
        @DstructBf = ptr
          @save=[]			
            @count=0

  def DstructBf			
	@filename=""			#filestream
	@ip=""                          #socketstream
	@port=""
	@file=0
        @sock=0
  end

  def flag
	@fileflag=0			#flags to check the current condition
	@sockflag=0			
  end

   def a 
	 @ptr=@ptr+1				#move the pointer one position to the right		
     @ptr=0 if @ptr==30000			
   end

  def b
	@ptr=@ptr-1				#move the pointer one position to the left
	@ptr=29999 if @ptr==-1			
  end


   def c
	 @machine[@ptr]+=1			#increment the value of the current cell
   end

   def d
     @machine[@ptr]-=1		         	#decrement  the value of the current cell
   end

   def e
	  @machine[@ptr]=STDIN.getc		#get a "character" from the input
   end

   def f
      puts"@machine[@ptr].chr"		#print a "character" to the output
   end

   def j						#if instruction is [ place the location of 
	 if @machine[@ptr]==0 && @count==0
	     until $buff[$i]== 'k'
	         $i+=1
	   if @machine[@ptr]==0 && @count != 0
	       $i=@save[@count]
	       @count-=1
	      @count+=1
	      @save[@count]=$i
	   end

   def k
      if(@machine[@ptr])!=0 then			#if instruction is ] and content is non zero
        $i=@save[@count]     			# get the location 
        @count-=1					#else pop the stack     

include Flags					#including Bfpp Flags via mixins

  def initialize
    @super						#initializing the parent class Bf
     @nit_Dsbfpp					#Initializing Bf data structures
     @flag						#Initializing Bf flags

  def l			   			#extracting the filename from the turing and opening the file 					
    old=@ptr					#save current pointer
       @ptr+=@machine[@ptr]			#change pointer to the offset
    while @machine[@ptr] != 0 		#extracting the filename	
         @filename<<@machine[@ptr].chr    	
	        @ptr+=1
             @ptr=0 if @ptr==30000
             
               #@ptr=old
     if @fileflag ==  0			#checking if a file is open/close
          if File.exists?(@filename)
	        if @file= File.open(@filename,"r+")	#if file exists open in appending mode
	           @file= File.new(@filename,"w+")	#else open in writing mode	
	              @fileflag=1				#set fileflag
	                 @file.close				#if already opened, close it
   
  def m						#File Reading: Reading one character at a time into the turing machine for each ":"
     value=@file.getc				#Reading a character from the file and incrementing the filepointer
      if value == NIL 
	    @machine[@ptr]=0			#placing 0 to ptr if EOF
      else
	    @machine[@ptr]=value			#placing value frm the file.
 
  def n						#writing one character from the turing machine to the opened file for each ";"
	save=@file.tell				#save existing filepointer
	@file.seek(0,IO::SEEK_END)		#move to EOF
	@file.putc(@machine[@ptr].chr)		#put data
	@file.seek(save,IO::SEEK_SET)		#come back to the old location
  end

  def o						# open socket
	if @sockflag == 0			#checking if socket is open
	  old=@ptr				#extracting i/p and port in the form
	  @ptr+=@machine[@ptr]			#addr=ip:port
	  addr=""
		  while @machine[@ptr] != 0
		    addr<<@machine[@ptr].chr
		    @ptr+=1
		  end
		  @ip, @port= addr.split(":") 	#spliting ip and port
	  @ptr=old
	  @sock = TCPSocket.new(@ip,@port)	#opening socket
	  @sockflag=1				#setting socket flag

	else
	  @sock.close				#if already open close it.
	  @ip=""				#clear the ip
	  @port=""
	end
  end

  def p						#read from socket 
	x=@sock.getc				#read a character from socket
	  if @sock.getc == 4			#place 0 to ptr if EOF
	   @machine[@ptr]=0
	 @machine[@ptr]=x			#else place the character
  
  def q
	x=@machine[@ptr].chr			#write to socket
	@sock.putc(x)
  end


  def r
        "DstructBf".STDIN.gets.chomp? bf #required without exception as it needs to catch the old character from bf output. 
          puts "Current pointer: " + @ptr.to_s		#print the current pointer location.
            ti=$i+1
            size=$buff.size - $i
          if size > 5
            size = $i+6
         print "Next 5 instructions: "			#print next five instructions or the next instructions which ever is smaller.
  while ti < siz
          print $buff[ti].chr.tr('abcdefjklmnopqrs','><+\-,.[]#:;%^!D=')
             ti+=1
  end
          puts ""
           print "Enter range: "				#accept the range of the tape to be displayed.
            	range=STDIN.gets.chomp
	                x,y=range.split("-")			#split it with the hyphen  
	                 x=x.to_i
	                  r=x
                     	y=y.to_i+1
	
	     until x == y do				#display the range of values
	          print @machine[x]
	            print " | "
	            x+=1
	     end
	         puts "\n"
	          print "EDIT(y/n)?"			#ask user for edit?
	             answer=STDIN.gets.chomp
                 	x=r
             	if answer == 'y'				#if yes accept the new values to machine[x] to machine[y]
	              print "Enter the data in ascii:"
	      if x == y
	          @machine[x]=STDIN.gets.chomp.to_i
	             x+=1
	          x=r
	           x=x.to_i
	         if x == y				#display the new values.
	            print @machine[x]
	              print " | "
	                 x+=1
end
 
