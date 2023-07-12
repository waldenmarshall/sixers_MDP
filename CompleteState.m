classdef CompleteState
    properties (SetAccess = protected)
      cur_score (1,1) uint8 {mustBeInteger, mustBeNonnegative,...
          mustBeLessThanOrEqual(cur_score, 36)} ...
          =cast(0,'uint8')%sum of dice kept
      turn (1,1) {mustBeInteger, mustBePositive,...
          mustBeLessThanOrEqual(turn, 3)} ...
          =cast(1,'uint8')%roll number 1,2,3
      dice (:,1) uint8 {mustBeInteger, mustBeNonnegative,...
          mustBeLessThanOrEqual(dice, 6)} ...
          =cast(zeros(6,1),'uint8')%ordered multiset of dice in play
    end
   methods
       function self = MDPstate()
           %constructor for looping creating entire single player state
           self.cur_score = 0;
           self.turn =  1;
           self = self.roll(6);
       end
       function self = updateState(self, k) %k: num to keep
           if self.turn == 3
               error('Error: No decision made at t=3')
           elseif k > diceInPlay(self)
               error('Error: you cannot keep more dice than are in play')
           elseif k< 1
               if diceInPlay(self) ~= 0 || self.turn ~= 2
                    error(['Error: you must keep at least one die on each turn unless you kept them' ...
                   'all in turn 1'])
               end
           end
           self.cur_score = self.cur_score + sum(self.dice(1:k));
           self.turn = self.turn + 1;
           self = roll(self, diceInPlay(self) - k);
       end
       function self = roll(self, numdice) %numdice: num to roll
            r = randi(6,[numdice,1]);
            r(r==3) = 0;
            self.dice = cast( sort(r), 'uint8' );
       end
       function dip = diceInPlay(self)
           dip=cast(length(self.dice), 'uint8');
       end
   end
end