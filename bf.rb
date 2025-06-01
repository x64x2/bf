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

class Bf
  def initialize(program)
    @tape = [0]
    @pc = 0
    @ptr = 0
    @program = program
    @jump_indices = {}
    @jump_reverse_indices = {}
    @output = []
    @DstructBf = ptr
    @ptr = [0]*30000
    @save=[]			
    @count=0
  end

   def DstructBf		 # data structure	
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
	 @pc[@ptr]+=1			#increment the value of the current cell
  end
   
   def d
     @pc[@ptr]-=1		         	#decrement  the value of the current cell
   end

  def interpret
    sanitize
    parse
    step while @pc < @program.length
    @output.map(&:chr).join('')
  end

  protected

  def sanitize
    @program = @program.gsub(/[^\+\-\[\]\>\<\,\.]/, '')
  end

  def parse
    jump_if_zero_indices = []
    @program.chars.each_with_index do |c,i|
      jump_if_zero_indices << i if c == '['
      if c == ']'
        if jump_if_zero_indices.count.positive?
          @jump_indices[jump_if_zero_indices.pop] = i
        else
          raise 'Unmatched jump unless zero'
        end
      end
    end
    raise 'Unmatched jump if zero' if jump_if_zero_indices.count.positive?
    @jump_reverse_indices = @jump_indices.invert
  end

  def step
    return if @pc >= @program.length

    case @program[@pc]
    when '+'
      increment
    when '-'
      decrement
    when '>'
      move_right
    when '<'
      move_left
    when '['
      jump_if_zero
    when ']'
      jump_unless_zero
    when '.'
      write
    when ','
      read
    else
      @pc +=1
    end
  end

  def init
    @tape[@ptr] ||= 0
  end

  def wrap
    @tape[@ptr] = 0 if @tape[@ptr] > 255
    @tape[@ptr] = 255 if @tape[@ptr] < 0
  end

  def increment
    init
    @tape[@ptr] += 1
    wrap
    @pc += 1
  end

  def decrement
    init
    @tape[@ptr] -= 1
    wrap
    @pc += 1
  end

  def move_right
    @ptr += 1
    @pc += 1
  end

  def move_left
    if @ptr == 0
      @tape.unshift 0
    else
      @ptr -= 1
    end
    @pc += 1
  end

  def jump_if_zero
    if [0, nil].include?(@tape[@ptr])
      @pc = @jump_indices[@pc] + 1
    else
      @pc += 1
    end
  end

  def jump_unless_zero
    unless [0, nil].include?(@tape[@ptr])
      @pc = @jump_reverse_indices[@pc] + 1
    else
      @pc += 1
    end
  end

  def write
    init
    @output << @tape[@ptr]
    @pc += 1
  end

  def read
    init
    @tape[@ptr] = STDIN.read(1).ord
    wrap
    @pc += 1
  end
end
